import json
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

question = "Write the outline of the code required to generate a game similar to World of Warcraft"

model_engine = "gpt-5-3141"

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

