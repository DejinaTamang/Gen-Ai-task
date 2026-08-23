from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

text ="""
I ordered a laptop two weeks ago. The laptop itself is good,
but the delivery was very late and customer support did not
respond to my messages.
"""

prompt = f"""
Analyze the following customer message.

Follow these steps:

1. Identify the main issue.
2. Determine whether the customer is satisfied or dissatisfied.
3. Decide whether the overall sentiment is Positive, Negative, or Neutral.

Return your answer in this format:

Main issue:
Customer feeling:
Final sentiment:

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

print(response.choices[0].message.content)