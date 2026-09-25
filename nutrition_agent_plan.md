# Nutrition Agentic AI Application — Development Plan
## Agentic AI Software Development Life Cycle (SDLC)

**Project Title:** NutriAgent — Personalised Nutrition Agentic AI Application  
**Model:** `qwen/qwen3.8-27b` via Groq API  
**Framework:** Flask (Python) + HTML/CSS/JavaScript  
**Date:** 2025  

---

## Table of Contents

1. [Problem Definition & Goal Setting](#1-problem-definition--goal-setting)
2. [Agent Design & Architecture](#2-agent-design--architecture)
3. [Data & Knowledge Sources](#3-data--knowledge-sources)
4. [Safety, Ethics & Guardrails](#4-safety-ethics--guardrails)
5. [System Prompt Engineering](#5-system-prompt-engineering)
6. [Backend Development](#6-backend-development)
7. [Frontend Development](#7-frontend-development)
8. [Integration & API Design](#8-integration--api-design)
9. [Testing & Validation](#9-testing--validation)
10. [Deployment & Operations](#10-deployment--operations)
11. [Monitoring & Continuous Improvement](#11-monitoring--continuous-improvement)
12. [File Structure](#12-file-structure)
13. [Setup Instructions](#13-setup-instructions)

---

## 1. Problem Definition & Goal Setting

### 1.1 Problem Statement
Many individuals struggle to access personalised, contextually relevant nutritional guidance due to geographic constraints, cost of professional dietitians, or lack of awareness about diet and health interactions. A scalable AI-powered nutrition assistant can bridge this gap.

### 1.2 Objectives
- Collect user profile data: name, age, diet preference, medical history, and location.
- Generate a personalised nutrition plan tailored to the user's profile.
- Provide a conversational agent assistant to answer common nutrition queries.
- Apply safety guardrails to prevent harmful medical or dietary advice.
- Maintain user privacy and data ethics.

### 1.3 Success Criteria
- Agent correctly personalises responses based on user profile (diet type, medical conditions, location).
- All responses include an appropriate medical disclaimer.
- Agent refuses to diagnose diseases, prescribe medications, or provide dangerous advice.
- Application is accessible via a browser with a clean, responsive UI.
- API key is never exposed in frontend or source code.

### 1.4 Stakeholders
| Stakeholder | Role |
|---|---|
| End Users | People seeking personalised nutrition guidance |
| Developers | Build, maintain and deploy the application |
| Healthcare Advisors | Validate guardrails and disclaimer content |
| Institution | Maharshi Mahesh Yogi Ramayan University |

---

## 2. Agent Design & Architecture

### 2.1 Agent Type
**Conversational Agentic AI** — Single-turn and multi-turn query handling with stateless session context per request.

### 2.2 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      Browser (Frontend)                      │
│  index.html  ─  User Profile Form + Agent Chat Interface    │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTP POST (JSON)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Flask Backend (app.py)                         │
│  ┌─────────────────┐   ┌──────────────────────────────────┐ │
│  │ /generate_plan  │   │ /chat                            │ │
│  │ (Nutrition Plan)│   │ (Conversational Agent)           │ │
│  └────────┬────────┘   └────────────┬─────────────────────┘ │
│           │                         │                        │
│  ┌────────▼─────────────────────────▼─────────────────────┐ │
│  │              Safety & Guardrail Layer                   │ │
│  │  - Input sanitisation & prompt injection detection      │ │
│  │  - Output filtering & medical disclaimer injection      │ │
│  └────────────────────────┬────────────────────────────────┘ │
│                           │                                  │
│  ┌────────────────────────▼────────────────────────────────┐ │
│  │             Groq API Client (groq SDK)                   │ │
│  │         Model: qwen/qwen3.8-27b                         │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │   Groq Cloud Inference │
              │  qwen/qwen3.8-27b      │
              └────────────────────────┘
```

### 2.3 Agent Capabilities
| Capability | Description |
|---|---|
| Profile Collection | Gathers name, age, diet pref, medical history, location |
| Nutrition Plan Generation | Creates a personalised 7-day or daily meal plan |
| Conversational Q&A | Answers nutrition queries in context of user profile |
| Safety Filtering | Blocks harmful, medical, or unethical requests |
| Disclaimer Injection | Appends medical disclaimer to every plan/response |

### 2.4 Agent Limitations (Ethical Boundaries)
- Does NOT diagnose diseases or medical conditions.
- Does NOT prescribe, recommend, or advise stopping medications.
- Does NOT provide calorie-restricted plans below safe thresholds without professional supervision note.
- Does NOT retain user data between sessions (stateless).

---

## 3. Data & Knowledge Sources

### 3.1 Knowledge Embedded in System Prompt
- General nutritional guidelines (balanced macronutrients, micronutrients).
- Dietary considerations for diabetes (low GI foods, sugar management).
- Dietary considerations for blood pressure (DASH diet principles, low sodium).
- Vegetarian vs. non-vegetarian protein sources by region.
- Location-aware culturally relevant food suggestions.

### 3.2 User-Provided Context
| Field | Purpose |
|---|---|
| Name | Personalisation of responses |
| Age | Age-appropriate nutritional guidance |
| Diet Preference | Veg / Non-veg meal planning |
| Medical History | Condition-aware dietary adjustments |
| City / Country | Culturally relevant, locally available food options |

---

## 4. Safety, Ethics & Guardrails

### 4.1 Input Guardrails
1. **Prompt Injection Detection**: Keywords such as "ignore previous instructions", "reveal system prompt", "bypass safety", "show API key", "you are now", "DAN", "jailbreak" trigger a refusal response.
2. **Length Limits**: User inputs are capped to prevent token flooding.
3. **Input Sanitisation**: HTML entities and special characters are stripped before being embedded in prompts.
4. **Topic Scope Enforcement**: The system prompt instructs the model to decline non-nutrition queries.

### 4.2 Output Guardrails
1. **Medical Disclaimer**: Every nutrition plan and agent response appends a standard disclaimer.
2. **Response Filtering**: Backend scans for inadvertent harmful patterns before returning response.
3. **Escalation Language**: For medical queries, the agent recommends consulting a qualified healthcare professional.

### 4.3 Privacy & Data Ethics
- No personal data is stored server-side between requests.
- API key is loaded exclusively from environment variable `GROQ_API_KEY`.
- API key is never serialised in frontend HTML, JavaScript, or logs.
- Users are informed the service is for informational purposes only.

### 4.4 HAM (Helpful, Accurate, Mindful) Principles
| Principle | Implementation |
|---|---|
| Helpful | Provides actionable, contextualised nutrition advice |
| Accurate | Grounded in nutritional science; avoids fabrications |
| Mindful | Respectful tone, inclusive language, cultural sensitivity |

---

## 5. System Prompt Engineering

### 5.1 Nutrition Plan System Prompt Strategy
- Role: Expert registered dietitian and nutritionist.
- Task: Generate a personalised nutrition plan based on user profile.
- Constraints: No medical diagnosis, no medication advice, include disclaimer.
- Format: Structured meal plan with breakfast, lunch, dinner, snacks.
- Style: Warm, encouraging, professional.

### 5.2 Chat Agent System Prompt Strategy
- Role: Friendly AI nutrition assistant.
- Task: Answer user nutrition queries in context of their stored profile.
- Constraints: Scope limited to nutrition, food, and healthy eating.
- Refusal: Politely decline medical diagnosis, prescription, and off-topic requests.
- Style: Conversational, empathetic, evidence-informed.

---

## 6. Backend Development

### 6.1 Technology Stack
| Component | Technology |
|---|---|
| Language | Python 3.9+ |
| Web Framework | Flask |
| AI SDK | groq (official Python SDK) |
| Environment Config | python-dotenv |
| CORS | flask-cors |

### 6.2 Key Endpoints
| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Serve the frontend HTML |
| `/generate_plan` | POST | Generate personalised nutrition plan |
| `/chat` | POST | Conversational agent query |

### 6.3 Guardrail Implementation
- `is_prompt_injection(text)` — Returns True if suspicious patterns detected.
- `sanitise_input(text)` — Strips HTML tags and limits character length.
- `add_disclaimer(text)` — Appends medical disclaimer to output.

---

## 7. Frontend Development

### 7.1 Technology Stack
| Component | Technology |
|---|---|
| Markup | HTML5 |
| Styling | CSS3 (inline, responsive) |
| Scripting | Vanilla JavaScript (ES6+) |
| Icons | Unicode / Emoji (no external CDN) |

### 7.2 UI Components
1. **Header** — Application title and tagline.
2. **User Profile Form** — Collects name, age, diet preference, medical conditions, city, country.
3. **Generate Plan Button** — Submits profile to `/generate_plan`.
4. **Nutrition Plan Display** — Renders the AI-generated plan.
5. **Agent Chat Interface** — Text input, send button, scrollable conversation window.
6. **Medical Disclaimer Banner** — Permanent, visible disclaimer on the page.

---

## 8. Integration & API Design

### 8.1 Groq API Integration
- SDK: `groq` Python package.
- Authentication: `GROQ_API_KEY` environment variable.
- Model: `qwen/qwen3.8-27b`.
- Parameters: temperature=0.7, max_tokens=2048.

### 8.2 Request/Response Contract

**POST /generate_plan**
```json
Request:  { "name": "", "age": 0, "diet": "", "medical": "", "city": "", "country": "" }
Response: { "plan": "...", "status": "success" }
```

**POST /chat**
```json
Request:  { "message": "", "profile": { "name": "", "age": 0, "diet": "", "medical": "", "city": "", "country": "" } }
Response: { "reply": "...", "status": "success" }
```

---

## 9. Testing & Validation

### 9.1 Test Scenarios
| Test Case | Expected Outcome |
|---|---|
| Valid veg profile with diabetes | Personalised low-GI vegetarian meal plan |
| Valid non-veg profile, no conditions | Balanced non-veg meal plan |
| Prompt injection attempt ("ignore instructions") | Refusal message returned |
| Off-topic query ("tell me a joke") | Polite redirect to nutrition topics |
| Request to diagnose a disease | Polite refusal + recommendation to consult doctor |
| Empty required fields | Validation error from frontend/backend |
| Missing API key | Clear error message, no crash |

### 9.2 Manual Testing Checklist
- [ ] Plan generates correctly for all diet types.
- [ ] Medical disclaimer appears on every response.
- [ ] Prompt injection is blocked.
- [ ] Chat retains user profile context during conversation.
- [ ] Application is mobile-responsive.
- [ ] API key never appears in browser developer tools network tab.

---

## 10. Deployment & Operations

### 10.1 Local Deployment (Windows)
- Run `setup_and_run.bat` to: create a virtual environment, install dependencies, and launch the Flask server.
- Access the application at `http://localhost:5000`.

### 10.2 Environment Configuration
- Copy `.env.example` to `.env`.
- Set `GROQ_API_KEY=your_actual_key_here`.

### 10.3 Dependencies
See `requirements.txt` for the complete list.

---

## 11. Monitoring & Continuous Improvement

### 11.1 Observability
- Flask logs all requests to console (stdout).
- Errors are caught and returned as JSON with appropriate HTTP status codes.

### 11.2 Future Enhancements
| Enhancement | Priority |
|---|---|
| Session-based conversation memory | High |
| Multi-language support | Medium |
| Grocery list generation from meal plan | Medium |
| Integration with food databases (USDA, OpenFoodFacts) | Low |
| User authentication and profile persistence | Low |

---

## 12. File Structure

```
Nutrition Website/
├── app.py                  # Flask backend with Groq API + guardrails
├── index.html              # Frontend UI (profile form + agent chat)
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── setup_and_run.bat       # Windows batch file for setup and launch
└── nutrition_agent_plan.md # This SDLC documentation file
```

---

## 13. Setup Instructions

### Step 1 — Get a Groq API Key
1. Visit [https://console.groq.com](https://console.groq.com) and sign up or log in.
2. Navigate to **API Keys** and create a new key.
3. Copy the key — it will only be shown once.

### Step 2 — Configure the API Key
1. In the project folder, copy `.env.example` to `.env`:
   ```
   copy .env.example .env
   ```
2. Open `.env` in any text editor.
3. Replace `your_groq_api_key_here` with your actual key:
   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
   ```

### Step 3 — Run the Application
1. Double-click `setup_and_run.bat` **or** run it from Command Prompt:
   ```
   setup_and_run.bat
   ```
2. The script will:
   - Check for Python installation.
   - Create a virtual environment (`venv`).
   - Install all required dependencies.
   - Start the Flask development server.
3. Open your browser and go to: **http://localhost:5000**

### Step 4 — Using the Application
1. Fill in your profile (name, age, diet preference, medical history, location).
2. Click **"Generate My Nutrition Plan"** to receive a personalised plan.
3. Use the **Agent Chat** panel to ask follow-up nutrition questions.

---

*© 2025 — Nutrition Agentic AI Application | Maharshi Mahesh Yogi Ramayan University*  
*Powered by Groq API · Model: qwen/qwen3.8-27b*
