from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

temperature = 0.8
max_tokens = 500

prompts = [
    "Explain what Artificial Intelligence is in simple words.",

    """Summarize the following paragraph in 3 sentences:
    Old man Miller kept a brass key on a string around his neck. For forty years,
    he never spoke of what the key opened. The neighborhood children whispered
    it unlocked a chest of gold, or perhaps a time machine. One rainy Tuesday,
    Miller fell ill. As the ambulance rolled away, young Leo found the dropped
    key on the porch. His heart raced. He crossed the threshold, climbed the
    creaking stairs to the third floor, and found the tiny padlock on the attic
    door. The key turned with a soft click. Leo pushed the door open. There was
    no gold. No magic. Just hundreds of birdcages, and in each one, a small
    mechanical clock ticking in a different rhythm. They filled the room with
    a gentle, breathing pulse of time. Miller wasn't hiding treasure. He was
    keeping the quiet seconds safe for the world.
    """,

    'Translate the following sentence into Korean: '
    '"Hello my name is Dejina Tamang. I am 20 years old. I love Hangeul."',

    "Solve this problem step by step: If a train travels 60 km in 1 hour, "
    "how far will it travel in 4 hours?",

    "Explain what is zero-shot learning?"
]

# Open file once and save all results
with open("zero_shot_results.txt", "w", encoding="utf-8") as f:

    for i, prompt in enumerate(prompts, start=1):

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        answer = response.choices[0].message.content

        print("\n" + "=" * 50)
        print(f"PROMPT {i}")
        print(prompt)

        print("\nRESPONSE:")
        print(answer)

        # Save to text file
        f.write("=" * 60 + "\n")
        f.write(f"PROMPT {i}\n")
        f.write(prompt + "\n\n")
        f.write("RESPONSE:\n")
        f.write(answer + "\n\n")

print("\nAll results saved to zero_shot_results.txt")