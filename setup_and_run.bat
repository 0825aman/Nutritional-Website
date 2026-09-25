@echo off
REM ============================================================
REM  NutriAgent — Nutrition Agentic AI Application
REM  Windows Setup and Launch Script
REM  Powered by Groq API · Model: qwen/qwen3.8-27b
REM ============================================================

title NutriAgent Setup and Launch

echo.
echo  ============================================================
echo   NutriAgent — Personalised Nutrition Agentic AI Application
echo  ============================================================
echo.

REM ---- Step 1: Check Python installation ----------------------
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo  ERROR: Python is not installed or not found in PATH.
    echo  Please install Python 3.9 or higher from https://www.python.org/downloads/
    echo  Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version 2^>^&1') do echo  Found: %%i
echo.

REM ---- Step 2: Check for .env file ----------------------------
echo [2/5] Checking environment configuration...
if not exist ".env" (
    if exist ".env.example" (
        echo  INFO: .env file not found. Copying .env.example to .env...
        copy ".env.example" ".env" >nul
        echo.
        echo  ************************************************************
        echo  *  ACTION REQUIRED:                                        *
        echo  *  Open the .env file in this folder and replace           *
        echo  *  "your_groq_api_key_here" with your actual Groq API key. *
        echo  *                                                           *
        echo  *  Get your key at: https://console.groq.com               *
        echo  ************************************************************
        echo.
        pause
    ) else (
        echo  WARNING: No .env or .env.example file found.
        echo  The application requires GROQ_API_KEY to be set in a .env file.
        echo.
    )
) else (
    echo  .env file found.
)
echo.

REM ---- Step 3: Create virtual environment ---------------------
echo [3/5] Setting up Python virtual environment...
if not exist "venv" (
    echo  Creating virtual environment (venv)...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo  ERROR: Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo  Virtual environment created.
) else (
    echo  Virtual environment already exists.
)
echo.

REM ---- Step 4: Install dependencies ---------------------------
echo [4/5] Installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo  ERROR: Failed to install dependencies.
    echo  Please check your internet connection and try again.
    pause
    exit /b 1
)
echo  Dependencies installed successfully.
echo.

REM ---- Step 5: Launch the application -------------------------
echo [5/5] Starting NutriAgent...
echo.
echo  ============================================================
echo   Application is starting at: http://localhost:5000
echo   Open your browser and go to: http://localhost:5000
echo.
echo   Press Ctrl+C to stop the server.
echo  ============================================================
echo.

python app.py

REM If server exits, pause so user can read any error messages
echo.
echo  Server stopped.
pause
