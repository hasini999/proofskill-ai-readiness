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
    "confidence_level": "High" if role == "Backend Developer" else "Medium",
    "score_reasoning": "Strong core programming skills but limited real-world deployment and design experience.",
    "strengths": [
        "Java and SQL fundamentals",
        "REST API development",
        "Backend project experience"
    ],
    "skill_gaps": [
        {
            "skill": "System Design",
            "recommendation": "Learn basic system design patterns and design a URL shortener"
        },
        {
            "skill": "Cloud Deployment",
            "recommendation": "Deploy a Spring Boot application on Google Cloud Run"
        }
    ],
    "weak_claims": [
        "Docker",
        "Microservices"
    ],
    "evidence": {
        "REST APIs": "Built backend services using Spring Boot",
        "SQL": "Used SQL databases in backend projects",
        "Java": "Developed backend applications using Java"
    }
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
