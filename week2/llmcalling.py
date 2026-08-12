import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"#request is sent to this endpoint
)

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Explain what is photosynthesis."
)

print(response.output_text)