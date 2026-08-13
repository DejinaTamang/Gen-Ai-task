import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"#request is sent to this endpoint
)

query=input("Enter your query: ")
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. onlyanswer question related to math "},
        {"role": "user", "content": query}
    ]
)

print(response.choices[0].message.content)