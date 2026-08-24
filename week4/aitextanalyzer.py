from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_text(text):

    prompt = f"""
You are an AI text analysis assistant.

Analyze the user's text and return structured information.

Tasks:
1. Create a short summary.
2. Identify the sentiment.
3. Identify the main category.
4. Extract the most important key points.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "summary": "short summary",
    "sentiment": "Positive, Negative, or Neutral",
    "category": "main category",
    "key_points": ["point 1", "point 2"]
}}

Rules:
- Do not add information that is not in the input.
- Keep the summary concise.
- Use one of Positive, Negative, or Neutral for sentiment.
- Return valid JSON only.

User text:
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

    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model."
        }

    required_fields = [
        "summary",
        "sentiment",
        "category",
        "key_points"
    ]

    for field in required_fields:
        if field not in data:
            return {
                "error": f"Missing field: {field}"
            }

    if data["sentiment"] not in [
        "Positive",
        "Negative",
        "Neutral"
    ]:
        return {
            "error": "Invalid sentiment value."
        }

    return data


def main():

    print("================================")
    print("       AI TEXT ANALYZER")
    print("================================")

    text = input("\nEnter your text:\n")

    if not text.strip():
        print("Please enter some text.")
        return

    result = analyze_text(text)

    print("\n===== RESULT =====")

    if "error" in result:
        print(result["error"])
        return

    print("\nSummary:")
    print(result["summary"])

    print("\nSentiment:")
    print(result["sentiment"])

    print("\nCategory:")
    print(result["category"])

    print("\nKey Points:")
    for point in result["key_points"]:
        print("-", point)


if __name__ == "__main__":
    main()