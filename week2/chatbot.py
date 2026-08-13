import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"#request is sent to this endpoint
)
# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a friendly AI tutor who explains concepts in simple language."
    }
]

print("Chatbot started! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Chatbot ended.")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.7,
        max_tokens=200
    )

    assistant_reply = response.choices[0].message.content

    print(f"\nBot: {assistant_reply}\n")

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )