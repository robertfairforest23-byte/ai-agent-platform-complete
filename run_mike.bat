@echo off
REM MIKE AI Agent - Text Mode Runner
REM Starts MIKE in text mode for user input

echo.
echo ====================================================
echo  MIKE AI Agent - Text Mode
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

REM Run MIKE in text mode
echo Starting MIKE in text mode...
echo Type 'help' for available commands
echo Type 'exit' or 'quit' to stop
echo.
echo ====================================================
echo.

python -m src.mike --text

if %errorlevel% neq 0 (
    echo.
    echo ERROR: MIKE encountered an error
    echo Please check the messages above
    pause
    exit /b 1
)

echo.
echo ====================================================
echo  MIKE stopped
echo ====================================================
echo.
pause
