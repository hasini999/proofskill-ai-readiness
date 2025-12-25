import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

role = "Backend Developer"
resume_text = """

Computer Science undergraduate with experience in Java, SQL, and REST APIs.
Built backend services using Spring Boot.
Basic knowledge of cloud concepts and RESTful services.

"""

prompt = f"""
You are an AI placement readiness evaluator.

Target Role: {role}

Resume:
{resume_text}

Provide:
- Readiness Score (0–100)
- Top 3 Strengths
- Top 3 Skill Gaps
- Actionable Next Steps
"""

response = model.generate_content(prompt)
print(response.text)
