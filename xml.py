prompt = """
<student_profile>
    <skills>
        Python
        HTML
        CSS
        JavaScript
        Problem Solving
    </skills>
</student_profile>

<instructions>
Recommend a suitable career domain based on the student's skills.
</instructions>

<output_format>
Give the career domain and a short reason.
</output_format>
"""

result = ask(prompt)

print("XML Prompting result:")
print(result)