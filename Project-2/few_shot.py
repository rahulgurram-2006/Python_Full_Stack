prompt = """
Classify the sentiment.

Example 1:
Review: I loved this movie.
Sentiment: Positive

Example 2:
Review: This movie was terrible.
Sentiment: Negative

Example 3:
Review: The movie was released yesterday.
Sentiment: Neutral

Now classify:

Review: I really enjoyed the meeting.

Sentiment:
"""

result = ask(prompt)

print("Few-shot result:", result)