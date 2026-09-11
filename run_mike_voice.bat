@echo off
REM MIKE AI Agent - Voice Mode Runner
REM Starts MIKE in voice mode with microphone input

echo.
echo ====================================================
echo  MIKE AI Agent - Voice Mode
echo ====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Activate virtual environment if it exists
if exist venv (
    call venv\Scripts\activate.bat
) else (
    echo WARNING: Virtual environment not found
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Check for microphone
echo Checking for microphone...
echo Note: Make sure your microphone is working and enabled
echo.

echo Starting MIKE in voice mode...
echo Speak clearly and naturally
echo Say 'help' to see available commands
echo Say 'exit' or 'quit' to stop
echo.
echo ====================================================
echo.

python -m src.mike --voice

if %errorlevel% neq 0 (
    echo.
    echo ERROR: MIKE encountered an error
    echo Possible issues:
    echo   - Microphone not connected or disabled
    echo   - Internet connection required for speech recognition
    echo   - Audio driver issues
    echo.
    echo Please check the messages above or use text mode:
    echo   run_mike.bat
    echo.
    pause
    exit /b 1
)

echo.
echo ====================================================
echo  MIKE stopped
echo ====================================================
echo.
pause
