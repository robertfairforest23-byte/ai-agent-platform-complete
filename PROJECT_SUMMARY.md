# MIKE AI Agent Platform - Complete

**Complete, production-ready MIKE AI Agent Platform** 🤖

A voice-activated, multi-agent AI personal assistant for Windows with:
- 🎤 Voice recognition and text-to-speech
- 🤖 Multi-agent architecture (Automation, Clock, Tasks, Assistant)
- ⏰ Multi-timezone digital clock with business hours
- ✅ Task management with JSON persistence
- 🖥️ Desktop automation and app launcher
- 💬 Conversation history and intent recognition

## 🚀 Quick Start

### Windows Users (Easiest)
```bash
# 1. Extract the ZIP file
# 2. Double-click setup.bat
# 3. Double-click run_mike.bat or run_mike_voice.bat
```

### Manual Installation
```bash
git clone https://github.com/robertfairforest23-byte/ai-agent-platform-complete.git
cd ai-agent-platform-complete
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m src.mike --text
```

## 📚 Documentation

- **README.md** - Complete documentation with architecture, features, and development guide
- **docs/QUICK_START.md** - 2-minute quick start
- **docs/SETUP_GUIDE.md** - Detailed installation and troubleshooting

## ✨ Features

✅ Voice & Text Input  
✅ Intent Recognition  
✅ Multi-Agent System  
✅ Application Launcher  
✅ Digital Clock (15+ zones)  
✅ Task Management  
✅ Conversation History  
✅ Async Architecture  

## 💻 Available Commands

```
# Applications
Open notepad, Open calculator, Open chrome, Open excel

# Clock
Show all clocks, What time in EST?, Business hours, Switch to 24 hour

# Tasks
Add task <title>, Show tasks, Complete task, Show statistics

# General
Help, How do you work?, Exit
```

## 🔧 Requirements

- Windows 10/11
- Python 3.9+
- 4GB RAM (8GB recommended)
- Microphone (optional, for voice mode)
- Internet connection

## 📦 Project Structure

```
src/
  mike.py                    # Main MIKE agent
  digital_clock.py           # Multi-timezone clock
  todo_list.py              # Task management
  agents/
    base_agent.py           # Abstract agent class
    automation_agent.py      # App launcher
    clock_agent.py          # Clock commands
    todo_agent.py           # Task commands
    assistant_agent.py      # General Q&A

docs/
  QUICK_START.md            # Quick reference
  SETUP_GUIDE.md            # Installation guide

setup.bat                    # Automatic setup
run_mike.bat                 # Text mode runner
run_mike_voice.bat           # Voice mode runner
```

## 🎯 Usage Examples

**Text Mode**
```
You: Open notepad
MIKE: ✅ Opened notepad

You: Show all clocks
MIKE: [Displays 15+ time zones with current time]

You: Add task Buy groceries high
MIKE: ✅ Added task: Buy groceries
```

**Voice Mode**
```
MIKE: 🎤 Listening...
You: "Open calculator"
MIKE: ✅ Opened calculator
```

## 📖 Documentation

Full documentation available in:
- **README.md** - Complete guide with architecture, API reference, and development
- **docs/QUICK_START.md** - Get started in 2 minutes
- **docs/SETUP_GUIDE.md** - Detailed installation and troubleshooting

## 🤝 Contributing

Want to contribute? Great!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🛣️ Roadmap

### Version 2.0 (Next)
- [ ] Web Dashboard
- [ ] REST API
- [ ] Database Support
- [ ] Email Integration
- [ ] Calendar Integration

### Version 3.0 (Future)
- [ ] Mobile App
- [ ] Cloud Sync
- [ ] Advanced AI Chat
- [ ] Cross-Platform Support

## 📝 License

MIT License - See LICENSE file for details

## 🙌 Credits

Created by AI Agent Development Team

---

**MIKE AI Agent - Your Personal Desktop Assistant** 🤖

*Making Windows automation easy, intelligent, and fun!*

👉 **[Start with Quick Start](docs/QUICK_START.md)** | 📖 **[Read Full Documentation](README.md)** | 🐛 **[Report Issues](https://github.com/robertfairforest23-byte/ai-agent-platform-complete/issues)**
