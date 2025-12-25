import json
import google.generativeai as genai

# ----------------------------
# CONFIG
# ----------------------------
USE_MOCK_OUTPUT = True   # Set False when using real API key

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-pro")

roles = ["Backend Developer", "Data Analyst"]

resume_text = """
Computer Science undergraduate with experience in Java, SQL, and REST APIs.
Built backend services using Spring Boot.
Basic knowledge of cloud concepts and RESTful services.
"""

with open("prototype/prompt.txt", "r") as f:
    base_prompt = f.read()

# ----------------------------
# EXECUTION
# ----------------------------
for role in roles:
    print(f"\nEvaluating role: {role}\n")

    if USE_MOCK_OUTPUT:
        mock_response = {
            "role": role,
            "readiness_score": 72 if role == "Backend Developer" else 45,
            "strengths": [
                "Java and SQL fundamentals",
                "REST API development",
                "Backend project experience"
            ],
            "skill_gaps": [
                "Cloud deployment",
                "System design",
                "Advanced analytics" if role == "Data Analyst" else "API security"
            ],
            "next_steps": [
                "Deploy a project on Google Cloud",
                "Practice role-specific interview questions",
                "Strengthen missing core skills"
            ]
        }

        print(json.dumps(mock_response, indent=2))

    else:
        prompt = f"""
{base_prompt}

Role: {role}

Resume:
{resume_text}
"""
        response = model.generate_content(prompt)
        print(response.text)
