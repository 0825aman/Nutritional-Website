# -*- coding: utf-8 -*-
# pip install gtts

"""
NutriAgent — Voiceover Generator
Uses gTTS for text-to-speech and ffmpeg for audio/video merging.
No pydub dependency — works on Python 3.14+.
"""

import os, sys, subprocess
from gtts import gTTS

FFMPEG = r"C:\Users\Edunet Foundation\AppData\Local\Temp\ffmpeg\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
VIDEO_IN  = "NutriAgent_Project_Video.mp4"
VIDEO_OUT = "NutriAgent_Project_Video_Voiced.mp4"
TMP_DIR   = "tts_tmp"

TOTAL_SECONDS = 150
NUM_SLIDES    = 18
SPF           = TOTAL_SECONDS / NUM_SLIDES   # seconds per slide = 8.333...

# ---------------------------------------------------------------------------
# Narration script — 18 slides
# ---------------------------------------------------------------------------
NARRATION = [
    # Slide 1 — Title
    ("Welcome to NutriAgent, a personalised Nutrition Agentic AI Application. "
     "Powered by the Groq API using the Qwen 3.8 billion parameter model. "
     "Developed at Maharshi Mahesh Yogi Ramayan University."),

    # Slide 2 — Table of Contents
    ("This presentation covers all thirteen phases of the Agentic AI Software "
     "Development Life Cycle, including problem definition, architecture, safety, "
     "backend and frontend development, testing, deployment, and a live application demo."),

    # Slide 3 — Phase 1: Problem Definition
    ("Phase 1: Problem Definition. Many individuals lack access to personalised "
     "nutritional guidance. NutriAgent bridges this gap using a scalable, "
     "accessible, and safe AI-powered nutrition assistant."),

    # Slide 4 — Phase 2: Architecture
    ("Phase 2: Agent Architecture. The system uses a four-layer stack: "
     "Browser frontend, Flask backend, Safety and Guardrail Layer, and the Groq API. "
     "The agent handles both plan generation and conversational chat queries."),

    # Slide 5 — Phase 3: Data & Knowledge
    ("Phase 3: Data and Knowledge Sources. Knowledge is embedded in system prompts "
     "covering general nutrition, diabetes-friendly low G.I. foods, "
     "blood pressure management, and culturally relevant foods based on user location."),

    # Slide 6 — Phase 4: Safety & Guardrails
    ("Phase 4: Safety, Ethics, and Guardrails. Twenty-four regex patterns detect "
     "prompt injection attacks, jailbreak attempts, and API key extraction. "
     "Every response carries a mandatory medical disclaimer. "
     "The agent follows H.A.M. principles: Helpful, Accurate, and Mindful."),

    # Slide 7 — Phase 5: Prompt Engineering
    ("Phase 5: System Prompt Engineering. Two system prompts are used: "
     "one for nutrition plan generation as an expert registered dietitian, "
     "and one for the conversational chat agent. "
     "Both enforce strict safety boundaries and medical ethics."),

    # Slide 8 — Phase 6: Backend
    ("Phase 6: Backend Development. The Flask app provides three endpoints: "
     "root, generate plan, and chat. "
     "Three guardrail functions handle injection detection, input sanitisation, "
     "and disclaimer injection. The Groq API key is loaded only from an environment variable."),

    # Slide 9 — Phase 7: Frontend
    ("Phase 7: Frontend Development. The interface uses pure HTML 5, CSS 3, and JavaScript. "
     "It includes a profile form, a markdown renderer for AI responses, "
     "a typing indicator, six quick-query chips, and a fully responsive mobile layout."),

    # Slide 10 — Phase 8: API Integration
    ("Phase 8: API Integration. The Groq API is called with temperature 0.7 "
     "and up to 2048 tokens for plans and 1024 for chat. "
     "JSON request and response contracts are defined for both endpoints."),

    # Slide 11 — Phase 9: Testing
    ("Phase 9: Testing and Validation. Sixty-six test cases were run across "
     "twelve evaluation categories. All ten injection attacks were blocked. "
     "Disclaimers appeared on every response. "
     "Average chat latency was under three seconds. "
     "Overall agent correctness scored eighty-eight percent."),

    # Slide 12 — Phase 10 & 11: Deployment & Monitoring
    ("Phases 10 and 11: Deployment and Monitoring. On Windows, the setup and run dot bat "
     "script automates virtual environment creation, dependency installation, and server launch. "
     "The app can also be deployed to Render or Railway via GitHub."),

    # Slide 13 — Phase 12 & 13: File Structure & Setup
    ("Phases 12 and 13: File Structure and Setup. The project contains eight files. "
     "The GitHub repository is public at github.com slash 0825aman slash Nutritional-Website. "
     "Setup takes just three steps: get a Groq API key, configure the dot env file, "
     "and run the bat script."),

    # Slide 14 — Screenshot: Home Page
    ("Application Screenshot 1: The Home Page shows the green NutriAgent header, "
     "a permanent medical disclaimer banner, and the profile form collecting "
     "name, age, diet preference, medical history, city, and country."),

    # Slide 15 — Screenshot: Nutrition Plan
    ("Application Screenshot 2: The AI-Generated Nutrition Plan for Priya, "
     "a 32-year-old vegetarian from Mumbai with Type 2 Diabetes. "
     "The plan includes culturally relevant Indian foods, low G.I. options, "
     "and a complete daily meal schedule with a medical disclaimer appended."),

    # Slide 16 — Screenshot: Agent Chat
    ("Application Screenshot 3: The Agent Chat Interface. "
     "A valid nutrition query receives a detailed, profile-aware answer. "
     "Below it, a prompt injection attempt is immediately detected by the guardrail "
     "and blocked with a polite refusal message, demonstrated live."),

    # Slide 17 — Screenshot: Mobile & Files
    ("Application Screenshot 4: Mobile Responsive View. "
     "The two-column layout collapses to single column on small screens. "
     "The file listing shows all project files on GitHub "
     "with sizes from 64 bytes for requirements to 26 kilobytes for the frontend."),

    # Slide 18 — Thank You
    ("Thank you for watching. NutriAgent demonstrates a complete Agentic AI application "
     "built across thirteen SDLC phases, with twenty-four safety guardrails, "
     "one hundred percent disclaimer compliance, and sub-three-second response latency. "
     "Developed at Maharshi Mahesh Yogi Ramayan University, powered by Groq and Qwen."),
]

assert len(NARRATION) == NUM_SLIDES, f"Need {NUM_SLIDES} narrations, got {len(NARRATION)}"

def run(cmd, label=""):
    """Run a subprocess command; exit on failure."""
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"ERROR in {label}:\n{r.stderr[-800:]}")
        sys.exit(1)
    return r

# ---------------------------------------------------------------------------
# Step 1 — Generate per-slide MP3 via gTTS
# ---------------------------------------------------------------------------
os.makedirs(TMP_DIR, exist_ok=True)
print(f"\n[1/4] Generating TTS for {NUM_SLIDES} slides...")

mp3_files = []
for i, text in enumerate(NARRATION, start=1):
    mp3 = os.path.join(TMP_DIR, f"slide_{i:02d}.mp3")
    if not os.path.exists(mp3):
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save(mp3)
        print(f"  [{i:2d}/{NUM_SLIDES}] generated  ({len(text)} chars)")
    else:
        print(f"  [{i:2d}/{NUM_SLIDES}] cached")
    mp3_files.append(mp3)

# ---------------------------------------------------------------------------
# Step 2 — Pad / trim each MP3 to exactly SPF seconds using ffmpeg
# ---------------------------------------------------------------------------
print(f"\n[2/4] Fitting each clip to {SPF:.3f}s...")
padded_files = []
for i, mp3 in enumerate(mp3_files, start=1):
    out = os.path.join(TMP_DIR, f"padded_{i:02d}.mp3")
    # atrim + apad: trim to SPF, then pad silence if shorter
    cmd = [
        FFMPEG, "-y",
        "-i", mp3,
        "-af",
        f"atrim=end={SPF:.4f},apad=whole_dur={SPF:.4f}",
        "-ar", "44100", "-ac", "1",
        out,
    ]
    run(cmd, f"pad slide {i}")
    padded_files.append(out)
    print(f"  [{i:2d}/{NUM_SLIDES}] padded to {SPF:.3f}s")

# ---------------------------------------------------------------------------
# Step 3 — Concatenate all padded clips using ffmpeg concat filter
# ---------------------------------------------------------------------------
print(f"\n[3/4] Concatenating {NUM_SLIDES} clips into full voiceover...")
concat_list = os.path.join(TMP_DIR, "concat.txt")
with open(concat_list, "w") as f:
    for pf in padded_files:
        abs_pf = os.path.abspath(pf).replace("\\", "/")
        f.write(f"file '{abs_pf}'\n")

full_audio = os.path.join(TMP_DIR, "voiceover_full.mp3")
run([
    FFMPEG, "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    full_audio,
], "concat audio")

size_audio = os.path.getsize(full_audio)
print(f"  Full audio: {full_audio}  ({size_audio:,} bytes)")

# ---------------------------------------------------------------------------
# Step 4 — Merge voiceover audio with video
# ---------------------------------------------------------------------------
print(f"\n[4/4] Merging voiceover into video...")
run([
    FFMPEG, "-y",
    "-i", VIDEO_IN,
    "-i", full_audio,
    "-map", "0:v:0",
    "-map", "1:a:0",
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "128k",
    "-shortest",
    "-movflags", "+faststart",
    VIDEO_OUT,
], "merge video+audio")

# ---------------------------------------------------------------------------
# Done
# ---------------------------------------------------------------------------
size_mb = os.path.getsize(VIDEO_OUT) / (1024 * 1024)
print(f"\n  Voiceover video created successfully!")
print(f"  Output  : {os.path.abspath(VIDEO_OUT)}")
print(f"  Size    : {size_mb:.2f} MB")
print(f"  Slides  : {NUM_SLIDES}")
print(f"  Duration: {TOTAL_SECONDS} seconds")
