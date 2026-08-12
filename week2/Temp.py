from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",

    messages=[
        {
            "role": "user",
            "content": "Explain artificial intelligence in simple words."
        }
    ],

    # Controls creativity/randomness
    temperature=0.7,

    # Maximum number of tokens in the generated response
    max_tokens=200
)

print(response.choices[0].message.content)