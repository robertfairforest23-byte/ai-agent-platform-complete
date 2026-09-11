# 📃 Setup Guide - MIKE AI Agent

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Methods](#installation-methods)
3. [Detailed Windows Setup](#detailed-windows-setup)
4. [Configuration](#configuration)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Hardware
- **CPU**: Dual-core or better (Intel i5/Ryzen 5 recommended)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space for installation + dependencies
- **Microphone**: Required for voice mode (optional for text mode)
- **Speakers**: Required for voice feedback

### Software
- **OS**: Windows 10 (Build 1909+) or Windows 11
- **Python**: Version 3.9, 3.10, 3.11, or 3.12
- **Internet**: Required for:
  - Speech recognition (Google API)
  - Text-to-speech synthesis
  - NLP models
  - Package installation

---

## Installation Methods

### Method 1: Automatic Setup (RECOMMENDED)

**Best for**: First-time users, Windows users

1. Extract the repository ZIP file
2. Double-click `setup.bat`
3. Wait for completion (~5-10 minutes)
4. Run `run_mike.bat` or `run_mike_voice.bat`

**What it does**:
- ✅ Checks Python installation
- ✅ Creates virtual environment
- ✅ Installs all dependencies
- ✅ Creates data directory

### Method 2: Manual Setup

**Best for**: Advanced users, troubleshooting

```bash
# 1. Navigate to repository
cd path/to/ai-agent-platform-complete

# 2. Create virtual environment
python -m venv venv

# 3. Activate it (Windows)
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create data directory
mkdir data

# 6. Copy environment template
copy .env.example .env

# 7. Run MIKE
python -m src.mike --text
```

---

## Detailed Windows Setup

### Step 1: Install Python

1. Visit https://www.python.org/downloads/
2. Download Python 3.9 or later
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH"
5. Click "Install Now"
6. Wait for completion
7. Close installer

**Verify installation**:
```cmd
python --version
```

Should show: `Python 3.9.x` or higher

### Step 2: Download Repository

1. Go to https://github.com/robertfairforest23-byte/ai-agent-platform-complete
2. Click "Code" button
3. Click "Download ZIP"
4. Extract to your desired location
   - Example: `C:\Users\YourName\Documents\ai-agent-platform-complete`

### Step 3: Run Setup

1. Open File Explorer
2. Navigate to the extracted folder
3. Double-click `setup.bat`
4. A Command Prompt will open
5. Wait for all steps to complete
6. Press any key to close when done

### Step 4: First Run

**Text Mode** (Recommended):
- Double-click `run_mike.bat`
- Type `help` to see commands
- Type `exit` to stop

**Voice Mode**:
- Double-click `run_mike_voice.bat`
- Speak clearly
- Say "exit" to stop

---

## Configuration

### Environment Setup

1. Copy `.env.example` to `.env`:
   ```cmd
   copy .env.example .env
   ```

2. Edit `.env` with your settings:
   - `MIKE_NAME` - Your assistant name
   - `MIKE_VOICE_ENABLED` - Voice mode toggle
   - `VOICE_RATE` - Speech speed (50-400)
   - `VOICE_LANGUAGE` - Language (en-US, en-GB, etc.)

### API Keys (Optional)

**For advanced features**:

1. **OpenAI API**:
   - Visit https://platform.openai.com/api-keys
   - Create API key
   - Add to `.env`: `OPENAI_API_KEY=sk-...`

2. **Google Cloud**:
   - Create project at https://console.cloud.google.com
   - Enable Speech-to-Text and Text-to-Speech APIs
   - Create service account key
   - Add path to `.env`: `GOOGLE_CLOUD_KEY=path/to/key.json`

---

## Verification

### Test Text Mode

```bash
python -m src.mike --text
```

Try these commands:
```
You: Open notepad
You: Help
You: Exit
```

### Test Voice Mode

```bash
python -m src.mike --voice
```

Speak:
- "Open calculator"
- "Help"
- "Exit"

### Test Clock

```bash
python -m src.mike --text
```

Command: `Show all clocks`

### Test Tasks

```bash
python -m src.mike --text
```

Commands:
- `Add task Buy groceries high`
- `Show tasks`
- `Show statistics`

---

## Troubleshooting

### "Python not found"

**Problem**: Command Prompt says Python is not found

**Solutions**:
1. Reinstall Python with "Add to PATH" checked
2. Restart computer after installation
3. Verify: Open new Command Prompt and type `python --version`
4. If still not working:
   ```bash
   C:\Users\YourName\AppData\Local\Programs\Python\Python311\python --version
   ```

### "ModuleNotFoundError"

**Problem**: "ModuleNotFoundError: No module named 'src'"

**Solutions**:
1. Make sure you're in the repository root directory
2. Check virtual environment is activated (look for `(venv)` in prompt)
3. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```
4. Delete `venv` folder and run `setup.bat` again

### "No module named 'speech_recognition'"

**Problem**: Dependencies not installed properly

**Solutions**:
1. Activate virtual environment:
   ```bash
   venv\Scripts\activate
   ```
2. Reinstall:
   ```bash
   pip install -r requirements.txt
   ```
3. Wait for all packages to install (can take 5+ minutes)

### Microphone Not Working

**Problem**: Voice mode doesn't recognize speech

**Solutions**:
1. Test microphone in Windows:
   - Settings → Sound → Input
   - Select correct microphone
   - Test recording

2. Check permissions:
   - Settings → Privacy & Security → Microphone
   - Enable for your app

3. Test with Python:
   ```bash
   python -c "import speech_recognition as sr; r = sr.Recognizer(); print('Ready')"
   ```

4. Use text mode instead:
   ```bash
   python -m src.mike --text
   ```

### Tasks Not Saving

**Problem**: Tasks disappear when closing MIKE

**Solutions**:
1. Check `data` folder exists in repository root
2. If not, create it manually
3. Check file permissions on `data/tasks.json`
4. Verify disk space available

### Slow Performance

**Problem**: MIKE runs slowly or lags

**Solutions**:
1. Close unnecessary programs
2. Check available RAM: at least 1GB free
3. Restart MIKE
4. Check internet connection (required for voice)
5. Disable unnecessary agents if needed

### Voice Recognition Not Working

**Problem**: "Speech recognition error"

**Solutions**:
1. Verify internet connection
2. Try again (sometimes Google API times out)
3. Check microphone is not muted
4. Speak louder and clearer
5. Reduce background noise
6. Update dependencies: `pip install -r requirements.txt --upgrade`

### Application Won't Open

**Problem**: "❌ Could not open <app>"

**Solutions**:
1. Verify application is installed
2. Try different app name
3. Check spelling (use lowercase)
4. Open manually to verify it works
5. Some apps may require full path

### "Permission Denied" Errors

**Problem**: File access errors

**Solutions**:
1. Run Command Prompt as Administrator
2. Check antivirus software isn't blocking MIKE
3. Ensure write permissions on repository folder
4. Try moving repository to Documents folder

---

## Getting Help

1. **Check the README.md** - Full documentation
2. **Run with debug flag**:
   ```bash
   python -m src.mike --text --debug
   ```
3. **Check error messages** - Often indicate the problem
4. **Create GitHub Issue** - Include error output

---

## Uninstallation

To remove MIKE:
1. Delete the entire repository folder
2. Python and dependencies remain (optional to uninstall)

To remove Python (if desired):
1. Settings → Apps → Installed apps
2. Find Python
3. Click and uninstall

---

## Next Steps

1. ✅ Run MIKE in text mode
2. 🤖 Try basic commands
3. 📋 Create a to-do list
4. 🎤 Test voice mode
5. 📖 Read full README.md

---

**Setup complete! Enjoy MIKE! 🤖✨**
