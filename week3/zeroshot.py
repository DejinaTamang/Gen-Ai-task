from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

prompts = [
    "Explain what Artificial Intelligence is in simple words.",
    
    """Summarize the following paragraph in 3 sentences:
     Old man Miller kept a brass key on a string around his neck. For forty years, he never spoke of what the key opened. The neighborhood children whispered it unlocked a chest of gold, or perhaps a time machine.One rainy Tuesday, Miller fell ill. As the ambulance rolled away, young Leo found the dropped key on the porch. His heart raced. He crossed the threshold, climbed the creaking stairs to the third floor, and found the tiny padlock on the attic door.The key turned with a soft click. Leo pushed the door open. There was no gold. No magic. Just hundreds of birdcages, and in each one, a small mechanical clock ticking in a different rhythm. They filled the room with a gentle, breathing pulse of time.Miller wasn't hiding treasure. He was keeping the quiet seconds safe for the world.y.
    """,

    'Translate the following sentence into korean : "Hello my name is Dejina Tamang .I am 20 years old. I love hangeul ."',

    'Write a complete e-commerce website in one response.',

    "Explain what is zero-shot learning?"
]

for i, prompt in enumerate(prompts, start=1):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    print(f"\n{'='*50}")
    print(f"PROMPT {i}")
    print(prompt)
    print("\nRESPONSE:")
    print(answer)

 #For saving the results to a text file

    with open("zero_shot_results.txt", "w", encoding="utf-8") as f:

       for i, prompt in enumerate(prompts, start=1):

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content

        f.write(f"\nPROMPT {i}\n")
        f.write(prompt + "\n\n")

        f.write("RESPONSE:\n")
        f.write(answer + "\n")
        f.write("\n" + "="*60 + "\n")