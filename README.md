# Natural language interface for database

Given the schema of tables and a natural language query, this program will return a well formatted SQL.

## Example

Check out the [example](example) folder for a working example.

## Generate Token from OpenAI

1. Follow instructions [here](https://beta.openai.com/docs/api-reference/authentication) to generate an API key
2. Create a .env file in the root directory of this project
3. Add the following line to the .env file: `OPENAI_API_KEY=<your api key>`

## Start server

```
python ./nlp-service.py
```

Built with 💗 @ Arcesium Hackathon 2022. Won the `Best Application of Data Analytics & Visualization` award in the hackathon. 
