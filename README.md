# 🤖 MIKE AI Agent - Personal AI Assistant Platform

## ⚡ Quick Start (30 seconds)

### For Windows Users:
1. **Download** the repository
2. **Double-click** `setup.bat`
3. **Follow** the wizard
4. **Done!** MIKE is running 🎉

---

## 📋 Table of Contents

- [What is MIKE?](#what-is-mike)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Running MIKE](#running-mike)
- [Architecture](#architecture)
- [Available Commands](#available-commands)
- [Modules & Agents](#modules--agents)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Development Guide](#development-guide)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 What is MIKE?

**MIKE** (Multi-Intelligent Knowledge Engine) is your personal AI assistant that runs on your Windows computer. It's a voice-activated, multi-agent platform designed for desktop automation, task management, and intelligent assistance.

MIKE can:
- 🖥️ **Open applications** - Launch any Windows app with voice or text
- 🎤 **Listen to voice commands** - Hands-free operation
- 💬 **Understand intent** - Know what you want to do
- 🌍 **Manage multiple time zones** - View world clocks
- 📝 **Track tasks** - To-do list with local storage
- 🤖 **Multi-agent system** - Specialized agents for different tasks
- 🔄 **Remember interactions** - Conversation history

---

## ✨ Features

### Core Features
✅ **Voice Recognition** - Speak commands naturally  
✅ **Text Commands** - Type instructions  
✅ **Application Launcher** - Open any Windows app  
✅ **Intent Recognition** - Understands what you want  
✅ **Desktop Automation** - Control your PC  
✅ **Conversation History** - Remembers interactions  

### Additional Features
✅ **Digital Clock** - View time in 15+ time zones  
✅ **To-Do List** - Manage tasks with local storage  
✅ **Multi-Agent System** - Specialized agents for tasks  
✅ **Business Hours Checker** - See working hours globally  
✅ **Task Statistics** - Track completion rate  
✅ **Agent Management** - Enable/disable agents dynamically  
✅ **Async Architecture** - Non-blocking concurrent operations  

---

## 🖥️ System Requirements

### Hardware
- **Processor**: Dual-core or better
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space
- **Microphone**: Optional (for voice mode)
- **Speakers**: Optional (for voice feedback)

### Software
- **OS**: Windows 10 or Windows 11
- **Python**: 3.9 or higher
- **Internet**: Required for speech recognition and voice synthesis

---

## 📥 Installation

### Method 1: Automatic Setup (EASIEST)

**1. Download Repository**
- Visit https://github.com/robertfairforest23-byte/ai-agent-platform-complete
- Click "Code" → "Download ZIP"
- Extract the folder

**2. Run Setup**
- Double-click `setup.bat`
- Follow the wizard
- Choose your preferred mode

**That's it!** ✨

### Method 2: Manual Setup

```bash
# 1. Clone repository
git clone https://github.com/robertfairforest23-byte/ai-agent-platform-complete.git
cd ai-agent-platform-complete

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run MIKE
python -m src.mike --text
```

---

## 🚀 Running MIKE

### Quick Start Scripts

**Text Mode (Recommended for First Time)**
```bash
Double-click: run_mike.bat
```

**Voice Mode (Requires Microphone)**
```bash
Double-click: run_mike_voice.bat
```

### Manual Command Line

**Text Mode**
```bash
python -m src.mike --text
```

**Voice Mode**
```bash
python -m src.mike --voice
```

**Debug Mode**
```bash
python -m src.mike --text --debug
```

---

## 🏗️ Architecture

### System Design

MIKE uses an **async-first, multi-agent architecture**:

```
┌─────────────────────────────────────────────────────────┐
│                    MIKE MAIN AGENT                      │
│  - Input Processing (Voice/Text)                        │
│  - Intent Recognition (NLPEngine)                       │
│  - Agent Dispatcher                                     │
│  - Conversation History                                 │
└────────────────┬────────────────────────────────────────┘
                 │
        ┌────────┼────────┬──────────────┐
        ▼        ▼        ▼              ▼
   ┌─────────┐ ┌──────┐ ┌────────┐  ┌──────────┐
   │ Clock   │ │ Todo │ │Autom.  │  │Assistant │
   │ Agent   │ │Agent │ │Agent   │  │ Agent    │
   └─────────┘ └──────┘ └────────┘  └──────────┘
        │        │        │              │
        ▼        ▼        ▼              ▼
   ┌─────────┐ ┌──────┐ ┌────────┐  ┌──────────┐
   │ Digital │ │ Todo │ │ Windows│  │   NLP    │
   │ Clock   │ │ List │ │ Auto.  │  │ Engine   │
   └─────────┘ └──────┘ └────────┘  └──────────┘
```

### Key Components

1. **MIKEAgent (src/mike.py)** - Main orchestrator
   - Voice/text input handling
   - Intent extraction
   - Agent dispatch
   - Conversation history

2. **VoiceEngine** - Speech I/O
   - Google Speech Recognition for transcription
   - pyttsx3 for text-to-speech

3. **NLPEngine** - Intent recognition
   - Keyword-based intent detection
   - Extensible intent mapping

4. **Agent System** - Specialized workers
   - BaseAgent (abstract)
   - AutomationAgent (app launching)
   - ClockAgent (time zones)
   - TodoAgent (task management)
   - AssistantAgent (general Q&A)

5. **Modules**
   - DigitalClock (timezone display, business hours)
   - TodoListManager (task persistence)

---

## 💬 Available Commands

### Opening Applications
```
Open notepad          → Opens Notepad
Open calculator       → Opens Calculator  
Open paint            → Opens Paint
Open explorer         → Opens File Explorer
Open chrome           → Opens Google Chrome
Open firefox          → Opens Firefox
Open word             → Opens Microsoft Word
Open excel            → Opens Microsoft Excel
Open cmd              → Opens Command Prompt
Open powershell       → Opens PowerShell
```

### Clock Commands
```
Show all clocks       → Display all time zones
What time in EST?     → Show time in Eastern timezone
Business hours        → Show working hours (9 AM - 5 PM)
Switch to 24 hour     → Change time format
Add timezone          → Add new time zone
```

### Task Commands
```
Add task <title>      → Add new task
Show tasks            → Display all tasks
Complete task <id>    → Mark task as complete
Show statistics       → Display task statistics
Delete task <id>      → Delete a task
```

### General
```
Help                  → Shows all commands
What can you do?      → Lists capabilities
How do you work?      → Explains MIKE
Exit / Quit           → Stops MIKE
```

---

## 📦 Modules & Agents

### MIKE Agent (`src/mike.py`)
Core agent that processes commands and manages other agents.

**Key Features:**
- Async voice/text loops
- Intent recognition
- Multi-agent dispatch
- Conversation history
- Graceful shutdown

### Digital Clock (`src/digital_clock.py`)
Multi-timezone clock system with business hours tracking.

**Supported Zones:**
- UTC, EST, CST, MST, PST
- GMT, CET, IST, JST, AEST
- SGT, HKT, NZST, Dubai, BRT

**Features:**
- View all time zones at once
- Get time in specific zone
- Calculate time differences
- Check business hours globally
- DST awareness

### To-Do List (`src/todo_list.py`)
Local task management with persistent JSON storage.

**Features:**
- Add/edit/delete tasks
- Mark tasks complete
- Set priority levels (low/medium/high)
- Filter by status or priority
- View statistics
- Save to local JSON file

### Clock Agent (`src/agents/clock_agent.py`)
MIKE integration for clock functionality.

**Commands:**
- Show all clocks
- View time in specific zone
- Display business hours
- Switch time formats
- Add/remove timezones

### Automation Agent (`src/agents/automation_agent.py`)
Handles Windows application launching and control.

**Features:**
- Launch applications
- Automate user actions
- Extensible app registry

### Todo Agent (`src/agents/todo_agent.py`)
Handles task management commands.

**Features:**
- Add tasks from voice/text
- Display task lists
- Mark tasks complete
- Show statistics

### Assistant Agent (`src/agents/assistant_agent.py`)
General-purpose assistant for Q&A.

---

## 🎮 Usage Examples

### Example 1: Basic Commands

```
👤 You: Open notepad
🤖 MIKE: ✅ Opened notepad

👤 You: Open calculator
🤖 MIKE: ✅ Opened calculator

👤 You: Help
🤖 MIKE: [Shows available commands]
```

### Example 2: Using Digital Clock

```python
from src.digital_clock import DigitalClock

clock = DigitalClock()
print(clock.display_all_clocks())
print(clock.display_business_hours())
```

### Example 3: Using To-Do List

```python
from src.todo_list import TodoListManager

todo = TodoListManager()
todo.add_task("Complete MIKE setup", priority="high")
print(todo.display_all_tasks())
print(todo.display_statistics())
```

### Example 4: Using Agents Programmatically

```python
import asyncio
from src.agents.automation_agent import AutomationAgent
from src.agents.clock_agent import ClockAgent

async def main():
    auto_agent = AutomationAgent()
    clock_agent = ClockAgent()
    
    # Open an application
    result = await auto_agent.process("open notepad")
    print(result['response'])
    
    # Show clocks
    result = await clock_agent.process("show all clocks")
    print(result['response'])

asyncio.run(main())
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file (copy from `.env.example`):

```env
# MIKE Agent Configuration
MIKE_NAME=MIKE
MIKE_VOICE_ENABLED=true
MIKE_AUTO_START=false
MIKE_DEBUG_MODE=false

# API Keys (Optional)
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_CLOUD_KEY=path/to/google_cloud_key.json

# Voice Settings
VOICE_RATE=150
VOICE_LANGUAGE=en-US

# Windows Automation
AUTOMATION_ENABLED=true
SAFE_MODE=false

# Storage
TASK_DATA_FILE=data/tasks.json
```

*(MIKE works without these - they're for advanced features)*

---

## 🐛 Troubleshooting

### Common Issues

**Python not found**
- Reinstall Python 3.9+ from python.org
- Check "Add Python to PATH" during installation
- Restart your computer after installation
- Verify: `python --version` in Command Prompt

**Modules not found**
- Activate virtual environment: `venv\Scripts\activate`
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Check Python version matches requirements (3.9+)

**Microphone not working**
- Check Windows Sound Settings
- Test microphone is working in Sound settings
- Verify app has microphone permission
- Use text mode instead: `python -m src.mike --text`

**Application won't open**
- Make sure application is installed
- Try different application name
- Check if app name is correct (use lowercase)
- Try opening manually to verify it works

**ImportError for modules**
- Make sure you're in the repo root directory
- Check `src/__init__.py` exists
- Verify virtual environment is activated

**No tasks loading**
- Check `data/` directory exists
- Check `data/tasks.json` is readable
- Try deleting `data/tasks.json` to reset

---

## 📈 Performance Tips

- **Faster startup**: Use `.bat` files instead of typing
- **Better voice**: Use a quality microphone
- **Less lag**: Close unnecessary programs
- **Stable**: Keep internet connection active
- **Smooth**: Keep dependencies updated

---

## 👨‍💻 Development Guide

### Creating Custom Agents

```python
from src.agents.base_agent import BaseAgent
from typing import Any, Dict

class CustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="CustomAgent",
            description="My custom agent description"
        )
    
    async def process(self, command: str) -> Dict[str, Any]:
        """Process commands"""
        if not self.enabled:
            return {'success': False, 'response': 'Agent disabled'}
        
        try:
            # Your logic here
            result = self.do_something(command)
            return {
                'success': True,
                'response': result,
                'agent': self.name
            }
        except Exception as e:
            return {'success': False, 'response': str(e)}
    
    async def do_something(self, command: str) -> str:
        # Implement your functionality
        return f"Done: {command}"
```

### Adding Custom Commands

1. Update `NLPEngine.intents` in `src/mike.py`
2. Add handler in `MIKEAgent._handle_intent()`
3. Create new agent if needed
4. Test with `python -m src.mike --text`

### Extending Applications List

```python
# In src/agents/automation_agent.py
self.applications = {
    'notepad': 'notepad.exe',
    'your_app': 'your_app.exe',  # Add here
    # ...
}
```

---

## 🤝 Contributing

Want to help improve MIKE?

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** with clear messages (`git commit -m 'Add amazing feature'`)
6. **Push** to the branch (`git push origin feature/amazing-feature`)
7. **Submit** a Pull Request

### Areas for Contribution
- Add more application launchers
- Enhance NLP/intent recognition
- Add calendar integration
- Create web dashboard
- Add email integration
- Improve voice recognition
- Add more time zones
- Cross-platform support

---

## 📖 Learning Resources

### Getting Started
- [Python Official Site](https://www.python.org)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Async Python](https://docs.python.org/3/library/asyncio.html)

### Libraries Used
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - Desktop automation
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Voice input
- [pyttsx3](https://pyttsx3.readthedocs.io/) - Text-to-speech
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [PyTorch](https://pytorch.org/) - ML framework
- [Transformers](https://huggingface.co/transformers/) - NLP models

---

## 📊 Project Status

- ✅ Core Features: Complete
- ✅ Digital Clock: Complete
- ✅ To-Do List: Complete
- ✅ Multi-Agent System: Complete
- ✅ Voice Recognition: Complete
- ✅ Desktop Automation: Complete
- ✅ Documentation: Complete
- 🔄 Web Dashboard: In Development
- 🔄 REST API: Planned
- 🔄 Database Support: Planned

---

## 🎯 Roadmap

### Version 2.0 (Next)
- [ ] Web Dashboard (FastAPI + Vue.js)
- [ ] REST API for remote control
- [ ] Database Support (PostgreSQL)
- [ ] Email Integration
- [ ] Calendar Integration
- [ ] Advanced Automation (macro recording)
- [ ] Plugin system

### Version 3.0 (Future)
- [ ] Mobile App (React Native)
- [ ] Cloud Sync
- [ ] AI Chat Integration (ChatGPT)
- [ ] Advanced ML Models
- [ ] Cross-Platform Support (Mac/Linux)
- [ ] Home automation control
- [ ] Custom voice training

---

## 💡 Pro Tips

1. **Keep MIKE running** in background while working
2. **Use batch files** for quick startup
3. **Test commands** before automating them
4. **Monitor logs** for errors and insights
5. **Back up your data** (tasks.json)
6. **Keep dependencies updated** regularly
7. **Use voice mode** for hands-free operation
8. **Create custom agents** for specific workflows
9. **Configure env variables** for advanced features
10. **Join the community** and share improvements

---

## 📞 Support

### Need Help?

1. **Check Documentation**
   - README.md - This file
   - docs/SETUP_GUIDE.md - Detailed setup
   - docs/QUICK_START.md - Quick reference

2. **Common Issues**
   - See "Troubleshooting" section above
   - Check GitHub Issues
   - Review error logs

3. **Report Issues**
   - Create an issue on GitHub
   - Include error messages and steps to reproduce
   - Attach relevant logs

---

## 📝 License

This project is open source and available under the MIT License.

See LICENSE file for details.

---

## 🙌 Credits

**MIKE AI Agent** was created by the AI Agent Development Team.

### Technologies Used
- Python 3.9+
- SpeechRecognition
- pyttsx3
- PyAutoGUI
- FastAPI
- PyTorch
- Transformers
- Pydantic
- pytz

---

## 🚀 Getting Started Right Now

### Option 1: Super Easy (Recommended)
```bash
# Just double-click this file:
setup.bat
```

### Option 2: Text Mode
```bash
python -m src.mike --text
```

### Option 3: Voice Mode
```bash
python -m src.mike --voice
```

---

## 📫 Stay Updated

- Star ⭐ this repository
- Watch 👀 for updates
- Follow for new features
- Contribute 🤝 to the project
- Join discussions

---

**MIKE AI Agent - Your Personal Desktop Assistant** 🤖

*Making Windows automation easy, intelligent, and fun!*

---

**Happy coding!** 🚀✨
