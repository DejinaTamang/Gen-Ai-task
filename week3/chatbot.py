from groq import Groq
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
temperature=0.3

max_tokens=500

# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a friendly AI assistant."
    }
]


def chat(user_input):

    # ADD USER MESSAGE TO HISTORY
    messages.append({
        "role": "user",
        "content": user_input
    })

    # SEND FULL HISTORY TO AI MODEL
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )

    # EXTRACT AI REPLY
    assistant_reply = response.choices[0].message.content

    # ADD AI REPLY TO HISTORY
    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply


# ==============================
# CHAT LOOP
# ==============================

print("================================")
print("       AI CHATBOT")
print("================================")
print("Type 'exit' to stop the chatbot.\n")

while True:

    # Get user input
    user_input = input("You: ")

    # Check for exit
    if user_input.lower() == "exit":
        break

    # Get AI response
    assistant_reply = chat(user_input)

    # Display AI response
    print(f"AI: {assistant_reply}\n")


# ==============================
# ASK FOR HISTORY
# ==============================

history_choice = input(
    "\nDo you want to see the conversation history? (yes/no): "
)

if history_choice.lower() == "yes":

    print("\n================================")
    print("     FULL CONVERSATION HISTORY")
    print("================================\n")

    for i, msg in enumerate(messages):

        role = msg["role"].upper()
        content = msg["content"]

        print(f"{i}. {role}: {content}")

else:

    print("\nChat ended. Goodbye!")