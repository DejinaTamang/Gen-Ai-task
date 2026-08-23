from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

text = """
I ordered a laptop two weeks ago. The laptop is good,
but the delivery was very late and customer support did
not respond to my messages.
"""

prompt = f"""
Analyze the following customer message.

Return ONLY valid JSON.

The JSON must contain exactly these fields:

{{
    "summary": "short summary",
    "sentiment": "Positive, Negative, or Neutral",
    "category": "main category",
    "key_points": ["point 1", "point 2"]
}}

Do not include markdown.
Do not include explanations outside the JSON.

Message:
{text}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

result = response.choices[0].message.content

print(result)

# Convert JSON text into Python dictionary
data = json.loads(result)

print("\nSummary:", data["summary"])
print("Sentiment:", data["sentiment"])
print("Category:", data["category"])
print("Key Points:", data["key_points"])