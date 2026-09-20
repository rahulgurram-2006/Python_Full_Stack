!pip install -q groq
api_key = userdata.get("GROQ_API_KEY").strip()

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-120b"


def ask(prompt, system="You are a helpful assistant."):
    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=512,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
prompt = """
Classify the sentiment of the following review as Positive, Negative, or Neutral.

Reply with only the label.

Review: I really enjoyed the meeting.

Sentiment:
"""

result = ask(prompt)

print("Zero-shot result:", result)