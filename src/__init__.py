"""
MIKE AI Agent Platform
Personal AI assistant with voice control and desktop automation
"""

__version__ = "1.0.0"
__author__ = "AI Agent Development Team"
__license__ = "MIT"

from src.mike import MIKEAgent, VoiceEngine, NLPEngine, WindowsAutomation, MIKEConfig
from src.digital_clock import DigitalClock, TimeFormat, TimeZoneInfo, ClockDisplay
from src.todo_list import TodoListManager, Task, TaskPriority, TaskStatus

__all__ = [
    'MIKEAgent',
    'VoiceEngine',
    'NLPEngine',
    'WindowsAutomation',
    'MIKEConfig',
    'DigitalClock',
    'TimeFormat',
    'TimeZoneInfo',
    'ClockDisplay',
    'TodoListManager',
    'Task',
    'TaskPriority',
    'TaskStatus',
]
