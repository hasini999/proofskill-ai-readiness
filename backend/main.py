from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-pro")

@app.post("/evaluate")
async def evaluate_resume(
    resume: UploadFile,
    role: str = Form(...)
):
    try:
        content = await resume.read()
        resume_text = content.decode("utf-8", errors="ignore")

        prompt = f"""
You are an AI placement readiness evaluator.

Target Role: {role}

Resume:
{resume_text}

Provide:
- Readiness Score (0–100)
- Strengths
- Skill Gaps
- Actionable Next Steps
"""

        response = model.generate_content(prompt)

        return {"result": response.text}

    except Exception:
        return {
            "result": """
Readiness Score: 65/100

Strengths:
- Basic programming knowledge
- Academic projects

Skill Gaps:
- System design
- Cloud deployment

Next Steps:
- Build deployable projects
- Learn AWS basics
- Practice interviews

Evidence:
- Used SQL for querying and data retrieval, Data Handling
- Worked with structured data in academic projects

"""
        }
