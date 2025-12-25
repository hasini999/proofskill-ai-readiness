# ProofSkill – AI Placement Readiness Verifier 🚀

ProofSkill is an AI-powered system that objectively evaluates a student’s placement readiness for a specific job role by analyzing their resume using Google Gemini API.

---

## 🎯 Problem Statement

Many students apply for jobs without knowing whether their current skills and experience match the expectations of the role. Existing platforms focus on resume formatting or generic feedback, but do not provide role-specific readiness validation.

---

## 💡 Proposed Solution

ProofSkill uses Google’s Generative AI to analyze a resume against a selected job role and provides:

- A placement readiness score
- Identified strengths
- Skill gaps
- Clear, actionable next steps to improve employability

This helps students make informed decisions before applying for jobs.

---

## 🧠 Key Features

- Resume upload (PDF / TXT)
- Role-based AI evaluation
- AI-generated readiness score (0–100)
- Strength & skill gap analysis
- Simple dashboard-style result display

---

## 🏗️ System Architecture

Frontend (HTML/CSS/JS)  
→ FastAPI Backend  
→ Google Gemini API  
→ AI Evaluation  
→ Readiness Dashboard

(Architecture diagram available in `/architecture` folder)

---

## 🧰 Technology Stack

### Google Technologies Used
- **Gemini API** – Core AI reasoning and evaluation
- **Google Generative AI Services** – Resume analysis and feedback generation
- **Google Cloud Run (Planned)** – Scalable backend deployment
- **Firebase (Planned)** – Authentication and user data storage

### Other Tools & Frameworks
- FastAPI (Python backend)
- HTML, CSS, JavaScript (Frontend)
- Git & GitHub

---

## 🤖 Google AI Tools Integrated

- **Gemini API**
- **Generative AI (LLM-based reasoning)**

Gemini is used to perform role-specific reasoning, scoring, and feedback generation based on resume content.

---

## 🔬 Prototype Scope

This repository contains a functional prototype developed for the **GDG InnovateX Hackathon** that demonstrates:

- Real resume upload
- Backend API for evaluation
- Integration with Gemini AI
- Dashboard-style result presentation

The prototype focuses on core logic and usability rather than a fully deployed production system.

---

## 🔮 Future Scope

- Mock interview simulation using AI
- Recruiter-side verification dashboard
- Skill-wise personalized learning roadmap
- Firebase authentication
- Cloud Run deployment for scalability
- Downloadable AI evaluation report (PDF)

---

## 👥 Team

**LogicSmiths**  
GDG InnovateX Hackathon – GDG On Campus BVRIT


