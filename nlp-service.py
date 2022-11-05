import argparse
import logging
import os
import sys
from pathlib import Path

import openai
from dotenv import load_dotenv
from flask import Flask, Response, request
from flask_cors import CORS

logger = logging.getLogger(__name__)
null = None
description = "Natural language interface for database queries"

app = Flask(__name__)
CORS(app)

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
openai.api_key = os.environ["OPEN_API_KEY"]


def get_args_parser():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-v", "--verbosity", help="Set logging level", default="INFO")
    return parser


def cleanup_response(response):
    response = response.replace("Output:", "")
    response = response.replace("Input:", "")
    response = response.trim()
    response = response.strip()
    return response.replace("Output:", "").strip()


def ask_ai(question):
    logger.info("Requesting OpenAI for %s" % question)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.7,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    response = response.choices[0].text
    clean_response = cleanup_response(response)
    return clean_response


@app.route("/api/askdata", methods=["POST"])
def ask_data():
    try:
        data = request.form
        logger.info(data["question"])
        response = ask_ai(data["question"])
        logger.info(response)
        return Response(response), 200
    except Exception as e:
        logger.error(e)
        return Response(), 500


# healthcheck call to make sure the server is running
@app.route("/api/healthcheck", methods=["GET"])
def healthcheck():
    return Response("200 Ok"), 200


def test():
    # http POST http://localhost:5000/api/askdata question="What is the average price of a house in the US?"
    pass


if __name__ == "__main__":
    parser = get_args_parser()
    args = parser.parse_args()

    logging.basicConfig(
        stream=sys.stdout,
        level=getattr(logging, args.verbosity),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    app.run(debug=True, host="0.0.0.0", port=7000)
    sys.exit(0)
# python ./FIXME: nlp-service.py
# python -m pydoc -w FIXME: nlp-service
