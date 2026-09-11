"""
MIKE Agent - Todo Agent Implementation
Handles task management commands
"""

import logging
from typing import Any, Dict
from src.agents.base_agent import BaseAgent
from src.todo_list import TodoListManager


class TodoAgent(BaseAgent):
    """Agent for task management"""
    
    def __init__(self):
        super().__init__(
            name="TodoAgent",
            description="Handles task management, to-do lists, and productivity tracking"
        )
        self.todo_manager = TodoListManager()
        self.logger = logging.getLogger(__name__)
    
    async def process(self, command: str) -> Dict[str, Any]:
        """Process todo-related commands"""
        self.logger.info(f"Processing todo command: {command}")
        
        if not self.enabled:
            return {
                'success': False,
                'response': 'Todo agent is disabled',
                'agent': self.name
            }
        
        try:
            command_lower = command.lower()
            
            # Add task
            if 'add task' in command_lower or command_lower.startswith('add '):
                # Extract task title and priority
                parts = command.split()
                if len(parts) > 2:
                    title = ' '.join(parts[2:])
                    priority = 'medium'  # Default priority
                    
                    # Check for priority keywords
                    if 'high' in command_lower:
                        priority = 'high'
                    elif 'low' in command_lower:
                        priority = 'low'
                    
                    task = self.todo_manager.add_task(title, priority)
                    return {
                        'success': True,
                        'response': f"✅ Added task: {title}",
                        'agent': self.name,
                        'command_type': 'add_task'
                    }
                else:
                    return {
                        'success': False,
                        'response': 'Please specify task title',
                        'agent': self.name
                    }
            
            # Show all tasks
            elif 'show tasks' in command_lower or 'list tasks' in command_lower or 'display tasks' in command_lower:
                response = self.todo_manager.display_all_tasks()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'show_all'
                }
            
            # Show statistics
            elif 'statistics' in command_lower or 'stats' in command_lower:
                response = self.todo_manager.display_statistics()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'statistics'
                }
            
            # Mark complete
            elif 'complete' in command_lower or 'done' in command_lower:
                tasks = self.todo_manager.get_all_tasks()
                if tasks:
                    # Mark most recent pending task as complete
                    for task in reversed(tasks):
                        if task.status == 'pending':
                            self.todo_manager.mark_complete(task.id)
                            return {
                                'success': True,
                                'response': f"✅ Marked complete: {task.title}",
                                'agent': self.name,
                                'command_type': 'mark_complete'
                            }
                    return {
                        'success': False,
                        'response': 'No pending tasks to complete',
                        'agent': self.name
                    }
                else:
                    return {
                        'success': False,
                        'response': 'No tasks available',
                        'agent': self.name
                    }
            
            # Help
            elif 'help' in command_lower or 'todo help' in command_lower:
                response = self._get_help_text()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'help'
                }
            
            # Default: show all tasks
            else:
                response = self.todo_manager.display_all_tasks()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'show_all'
                }
            
        except Exception as e:
            self.logger.error(f"Todo agent error: {e}")
            return {
                'success': False,
                'response': f"Error: {str(e)}",
                'agent': self.name
            }
    
    def _get_help_text(self) -> str:
        """Get help text for todo commands"""
        return """
📋 TODO AGENT - AVAILABLE COMMANDS:

✏️ Create Tasks:
  • "Add task <title>" - Create new task
  • "Add high task <title>" - Create high priority task
  • "Add low task <title>" - Create low priority task

📋 View Tasks:
  • "Show tasks" - Display all tasks
  • "List tasks" - Display all tasks
  • "Show statistics" - Display task statistics

✅ Manage Tasks:
  • "Complete task" - Mark most recent pending task as complete
  • "Done" - Mark most recent pending task as complete

❓ Help:
  • "Todo help" - Show this help message

Task Priorities: low, medium (default), high
Task Status: pending, in_progress, completed
        """
    
    def add_task_direct(self, title: str, priority: str = "medium") -> bool:
        """Add task directly (programmatic use)"""
        try:
            self.todo_manager.add_task(title, priority)
            return True
        except Exception as e:
            self.logger.error(f"Error adding task: {e}")
            return False
    
    def get_all_tasks(self):
        """Get all tasks"""
        return self.todo_manager.get_all_tasks()
    
    def get_task_count(self) -> int:
        """Get number of tasks"""
        return len(self.todo_manager.get_all_tasks())
