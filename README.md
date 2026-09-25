# 🥦 NutriAgent — Personalised Nutrition Agentic AI Application

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-API-orange)](https://console.groq.com)
[![Model](https://img.shields.io/badge/Model-qwen%2Fqwen3.8--27b-purple)](https://console.groq.com/docs/models)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> A web-based Agentic AI application that generates **personalised nutrition plans** and answers nutrition-related queries using the **Groq API** with the `qwen/qwen3.8-27b` model.

---

## 📸 Features

- 🧑‍💼 **User Profile Collection** — Name, age, diet preference, medical history, city and country
- 🥗 **Personalised Nutrition Plan** — AI-generated daily meal plan tailored to your profile
- 🤖 **Agent Chat Assistant** — Conversational AI for nutrition Q&A with quick-query chips
- 🛡️ **Safety Guardrails** — Prompt injection detection, input sanitisation, scoped system prompts
- ⚠️ **Medical Disclaimer** — Automatically appended to every AI response
- 📱 **Responsive UI** — Clean, mobile-friendly interface built with vanilla HTML/CSS/JS
- 🔐 **Secure API Key Handling** — Key loaded exclusively from environment variable, never exposed

---

## 🗂️ Project Structure

```
Nutritional-Website/
├── app.py                  # Flask backend — Groq API integration + guardrails
├── index.html              # Frontend — profile form + agent chat UI
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template (copy to .env)
├── setup_and_run.bat       # Windows one-click setup & launch script
├── nutrition_agent_plan.md # Agentic AI SDLC documentation
└── README.md               # This file
```

---

## ⚙️ Prerequisites

- **Python 3.9+** — [Download here](https://www.python.org/downloads/) *(check "Add Python to PATH")*
- **Groq API Key** — [Get one free at console.groq.com](https://console.groq.com)
- **Git** *(for cloning)* — [Download here](https://git-scm.com/downloads)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/0825aman/Nutritional-Website.git
cd Nutritional-Website
```

### 2. Configure Your API Key

Copy the example environment file and add your Groq API key:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Open `.env` and replace the placeholder:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

> 🔑 Get your free API key at [https://console.groq.com](https://console.groq.com) → **API Keys** → **Create new key**

### 3a. Windows — One-Click Launch

Double-click **`setup_and_run.bat`** or run from Command Prompt:

```cmd
setup_and_run.bat
```

This script will automatically:
- ✅ Check Python is installed
- ✅ Create a virtual environment
- ✅ Install all dependencies
- ✅ Start the Flask server

### 3b. Manual Setup (Windows / macOS / Linux)

```bash
# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### 4. Open in Browser

```
http://localhost:5000
```

---

## 🧭 How to Use

1. **Fill in your profile** — name, age, diet preference (vegetarian/non-vegetarian), any medical conditions (e.g. diabetes, hypertension), and your location.
2. **Click "Generate My Nutrition Plan"** — the AI creates a personalised daily meal plan for you.
3. **Use the Agent Chat** — ask follow-up questions or click a quick-query chip:
   - 🥜 High-protein vegetarian foods
   - 🍳 Diabetic-friendly breakfast
   - 🌾 Fibre-rich foods
   - 🍎 Healthy snack ideas
   - ❤️ Blood pressure diet tips
   - 🍗 Dinner suggestions

---

## 🛡️ Safety & Ethics

| Guardrail | Implementation |
|---|---|
| Prompt injection detection | 24 regex patterns — blocks jailbreak, system prompt extraction, API key fishing |
| Input sanitisation | HTML tags stripped, special chars escaped, 1000-char limit per field |
| Output disclaimer | Medical disclaimer appended to every AI response automatically |
| Scoped system prompt | Model instructed to refuse diagnosis, prescriptions, off-topic requests |
| API key isolation | Key only in `.env` → `os.environ`; never serialised in frontend or logs |

> This application follows **HAM principles** — Helpful, Accurate, and Mindful — and is intended for **informational purposes only**. It does not provide medical diagnosis or treatment advice.

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Serves the frontend HTML |
| `/generate_plan` | POST | Generates a personalised nutrition plan |
| `/chat` | POST | Conversational agent query |

### POST `/generate_plan`
```json
{
  "name": "Priya Sharma",
  "age": 32,
  "diet": "Vegetarian",
  "medical": "Type 2 Diabetes",
  "city": "Mumbai",
  "country": "India"
}
```

### POST `/chat`
```json
{
  "message": "What are good high-protein breakfast options?",
  "profile": { "name": "Priya", "diet": "Vegetarian", "medical": "Diabetes" }
}
```

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **AI Model** | `qwen/qwen3.8-27b` via Groq API |
| **Backend** | Python 3.9+ · Flask 3.x · flask-cors |
| **AI SDK** | `groq` (official Python SDK) |
| **Config** | `python-dotenv` |
| **Frontend** | HTML5 · CSS3 · Vanilla JavaScript (ES6+) |
| **Deployment** | Any Python-capable host (local, Render, Railway, etc.) |

---

## 🌐 Deploying to the Cloud

### Render (Free Tier)
1. Push this repo to GitHub.
2. Go to [render.com](https://render.com) → **New Web Service** → connect your GitHub repo.
3. Set **Build Command**: `pip install -r requirements.txt`
4. Set **Start Command**: `python app.py`
5. Add environment variable `GROQ_API_KEY` in the Render dashboard.

### Railway
1. Connect GitHub repo at [railway.app](https://railway.app).
2. Add `GROQ_API_KEY` as an environment variable.
3. Railway auto-detects Flask and deploys.

---

## ⚠️ Medical Disclaimer

> NutriAgent provides general nutrition information for **educational and informational purposes only**. It is **not** a substitute for professional medical or dietetic advice, diagnosis, or treatment. Always consult a qualified healthcare provider or registered dietitian before making significant dietary changes, especially if you have a medical condition or are taking medication.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🏫 About

Developed as part of the **Advanced GLE Session** at  
**Maharshi Mahesh Yogi Ramayan University**  
Powered by [Groq API](https://console.groq.com) · Model: `qwen/qwen3.8-27b`
