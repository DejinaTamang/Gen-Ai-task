from groq import Groq
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",

    messages=[
        {
            "role": "user",
            "content": """
Classify each review as Positive, Negative, or Neutral.

Example 1:
Review: "The movie was fantastic!"
Answer: Positive

Example 2:
Review: "The movie was boring and too long."
Answer: Negative

Example 3:
Review: "The movie was okay."
Answer: Neutral

Now classify:

Review: "I really enjoyed the movie. The acting was excellent."
Answer:
"""
        }
    ]
)

print(response.choices[0].message.content)