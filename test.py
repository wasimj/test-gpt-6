import json
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

question = "Write an Open Source version of the World of Warcraft game."

model_engine = "gpt-6-0141"

response = openai.ChatCompletion.create(
    model=model_engine,
    messages=[{"role":"user", "content": prompt}],
    max_tokens=32768,
    n=1,
    stop=None,
    temperature=0.8,
)

content = response.choices[0].message.content

print(content)

