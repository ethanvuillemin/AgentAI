# https://docs.mistral.ai/getting-started/quickstart/

import os
from mistralai import Mistral
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
api_key = os.environ["MISTRAL_API_KEY"]

model = "open-mistral-nemo"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ],
)
print(chat_response.choices[0].message.content)
