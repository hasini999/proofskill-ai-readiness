# ProofSkill – AI Placement Readiness Verifier

ProofSkill is a prototype AI system that evaluates a student’s placement readiness for a specific job role using **Google Gemini AI reasoning**.

The focus of this prototype is **AI-driven evaluation logic**, not UI or infrastructure.

---

## 🚀 Key Features

* Role-specific resume evaluation
* AI-generated readiness score
* Skill gap identification
* Actionable, role-aligned improvement guidance
* **Structured JSON output for system integration**
* **Role comparison using the same resume**

---

## 🧠 How It Works

1. A resume and target job role are provided as input
2. Gemini AI evaluates role alignment and skill coverage
3. The system returns a **structured JSON evaluation**
4. Multiple roles can be compared using the same resume

---

## 🔧 Google Technologies Used

* Google Gemini API
* Firebase (planned)
* Google Cloud Run (planned)

---

## 📦 Prototype Scope

This repository contains an early-stage prototype developed for the **GDG InnovateX Hackathon**.
It demonstrates:

* AI reasoning capability
* Role-aware evaluation
* Integration-ready output design

---

## ▶️ How to Run (Optional)

1. Add your Gemini API key in `prototype/app.py`
2. Update the resume text and target roles
3. Run:

   ```
   python prototype/app.py
   ```

> **Note:**
>
> * Mock execution mode is supported when an API key is not provided
> * Sample outputs are included for evaluation reference

---

## 📄 Sample Outputs

* `prototype/sample_output_backend.json`
* `prototype/sample_output_data_analyst.json`
* Execution screenshot available in `docs/demo_output.png`

---

## 🔮 Future Scope

* Mock interview simulations
* Multilingual resume evaluation
* Voice-based interaction
* Recruiter-side verification dashboard
