prompt = """
Recommend a suitable career domain for this student.

Follow these steps:

1. Identify the student's interests.
2. Identify suitable career domains.
3. Compare the domains.
4. Give one recommendation.

Student interests:
Python, web development, programming and problem solving.
"""

result = ask(prompt)

print("Step-by-step result:")
print(result)