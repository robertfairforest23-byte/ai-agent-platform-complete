@echo off
REM MIKE AI Agent - Windows Setup Script
REM Automatic setup wizard for MIKE AI Agent Platform

echo.
echo ====================================================
echo  MIKE AI Agent - Setup Wizard
echo ====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.9+ from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [1/5] Python found
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
echo This may take a few minutes...
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully
echo.

REM Create data directory
echo [5/5] Setting up data directory...
if not exist data (
    mkdir data
    echo Data directory created
) else (
    echo Data directory already exists
)
echo.

REM Setup complete
echo ====================================================
echo  Setup Complete!
echo ====================================================
echo.
echo You can now run MIKE AI Agent in two ways:
echo.
echo 1. Text Mode (Recommended):
echo    Double-click: run_mike.bat
echo.
echo 2. Voice Mode (Requires Microphone):
echo    Double-click: run_mike_voice.bat
echo.
echo Or manually from command line:
echo   python -m src.mike --text
echo   python -m src.mike --voice
echo.
echo ====================================================
echo.
pause
