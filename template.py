import argparse
import logging
import sys

logger = logging.getLogger(__name__)
null = None
description = "Natural language interface for database"


def get_args_parser():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-v", "--verbosity", help="Set logging level", default="INFO")
    return parser


if __name__ == "__main__":
    parser = get_args_parser()
    args = parser.parse_args()

    logging.basicConfig(
        stream=sys.stdout,
        level=getattr(logging, args.verbosity),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    sys.exit(0)
# python ./FIXME: nlp-service.py
# python -m pydoc -w FIXME: nlp-service
