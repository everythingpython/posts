import openlit
import pandas as pd
from openai import OpenAI
import os

openlit.init(
  otlp_endpoint="http://127.0.0.1:4318",
)

df = pd.read_csv("../data/Pokemon.csv")

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

message = [
    {"role": "system", "content": f"You are a data analyst. "
                                  f"Consider the data in {df} as markdown ."
                                  f"Answer the user's question. "
                                  f"Do not return code. Return the response concisely in markdown"},
    {"role": "user", "content": "Summarize the data "}
]

response = client.chat.completions.create(model="gpt-4o", messages=message, temperature=0.1)

print(response.choices[0].message.content)
