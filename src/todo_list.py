"""
To-Do List Manager for MIKE
Handles task management with local JSON persistence
"""

import json
import os
import logging
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum


class TaskPriority(Enum):
    """Task priority levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStatus(Enum):
    """Task status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task:
    """Represents a single task"""
    
    def __init__(self, title: str, priority: str = "medium", description: str = ""):
        self.id = datetime.now().timestamp()
        self.title = title
        self.priority = priority
        self.description = description
        self.status = TaskStatus.PENDING.value
        self.created_at = datetime.now().isoformat()
        self.completed_at: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'priority': self.priority,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary"""
        task = Task(data['title'], data['priority'], data.get('description', ''))
        task.id = data['id']
        task.status = data['status']
        task.created_at = data['created_at']
        task.completed_at = data.get('completed_at')
        return task
    
    def __str__(self) -> str:
        status_emoji = {
            'pending': '⏳',
            'in_progress': '⚙️',
            'completed': '✅'
        }
        priority_emoji = {
            'low': '🟢',
            'medium': '🟡',
            'high': '🔴'
        }
        return f"{status_emoji.get(self.status, '❓')} {priority_emoji.get(self.priority, '❓')} {self.title}"


class TodoListManager:
    """Main to-do list manager"""
    
    def __init__(self, data_file: str = "data/tasks.json"):
        self.data_file = data_file
        self.tasks: Dict[float, Task] = {}
        self.logger = logging.getLogger(__name__)
        
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(data_file) or "data", exist_ok=True)
        
        # Load existing tasks
        self._load_tasks()
    
    def _load_tasks(self) -> None:
        """Load tasks from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for task_data in data:
                        task = Task.from_dict(task_data)
                        self.tasks[task.id] = task
                self.logger.info(f"Loaded {len(self.tasks)} tasks from {self.data_file}")
        except Exception as e:
            self.logger.error(f"Error loading tasks: {e}")
    
    def _save_tasks(self) -> None:
        """Save tasks to JSON file"""
        try:
            task_data = [task.to_dict() for task in self.tasks.values()]
            with open(self.data_file, 'w') as f:
                json.dump(task_data, f, indent=2)
            self.logger.info(f"Saved {len(self.tasks)} tasks to {self.data_file}")
        except Exception as e:
            self.logger.error(f"Error saving tasks: {e}")
    
    def add_task(self, title: str, priority: str = "medium", description: str = "") -> Task:
        """Add a new task"""
        task = Task(title, priority, description)
        self.tasks[task.id] = task
        self._save_tasks()
        self.logger.info(f"Added task: {title}")
        return task
    
    def get_task(self, task_id: float) -> Optional[Task]:
        """Get a specific task"""
        return self.tasks.get(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return list(self.tasks.values())
    
    def get_tasks_by_status(self, status: str) -> List[Task]:
        """Get tasks by status"""
        return [task for task in self.tasks.values() if task.status == status]
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        """Get tasks by priority"""
        return [task for task in self.tasks.values() if task.priority == priority]
    
    def update_task(self, task_id: float, **kwargs) -> Optional[Task]:
        """Update task properties"""
        task = self.get_task(task_id)
        if task:
            if 'title' in kwargs:
                task.title = kwargs['title']
            if 'priority' in kwargs:
                task.priority = kwargs['priority']
            if 'description' in kwargs:
                task.description = kwargs['description']
            if 'status' in kwargs:
                task.status = kwargs['status']
            self._save_tasks()
            self.logger.info(f"Updated task: {task.title}")
            return task
        return None
    
    def mark_complete(self, task_id: float) -> bool:
        """Mark task as completed"""
        task = self.get_task(task_id)
        if task:
            task.status = TaskStatus.COMPLETED.value
            task.completed_at = datetime.now().isoformat()
            self._save_tasks()
            self.logger.info(f"Marked complete: {task.title}")
            return True
        return False
    
    def mark_in_progress(self, task_id: float) -> bool:
        """Mark task as in progress"""
        task = self.get_task(task_id)
        if task:
            task.status = TaskStatus.IN_PROGRESS.value
            self._save_tasks()
            self.logger.info(f"Marked in progress: {task.title}")
            return True
        return False
    
    def delete_task(self, task_id: float) -> bool:
        """Delete a task"""
        if task_id in self.tasks:
            task_title = self.tasks[task_id].title
            del self.tasks[task_id]
            self._save_tasks()
            self.logger.info(f"Deleted task: {task_title}")
            return True
        return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get task statistics"""
        total = len(self.tasks)
        completed = len(self.get_tasks_by_status(TaskStatus.COMPLETED.value))
        pending = len(self.get_tasks_by_status(TaskStatus.PENDING.value))
        in_progress = len(self.get_tasks_by_status(TaskStatus.IN_PROGRESS.value))
        
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'in_progress': in_progress,
            'completion_rate': f"{completion_rate:.1f}%"
        }
    
    def display_all_tasks(self) -> str:
        """Display all tasks in formatted view"""
        output = "\n📋 ALL TASKS\n"
        output += "=" * 70 + "\n"
        
        if not self.tasks:
            output += "No tasks yet. Add one with 'add task <title>'\n"
            output += "=" * 70 + "\n"
            return output
        
        # Group by status
        for status in [TaskStatus.COMPLETED.value, TaskStatus.IN_PROGRESS.value, TaskStatus.PENDING.value]:
            tasks = self.get_tasks_by_status(status)
            if tasks:
                status_display = {
                    'completed': '✅ COMPLETED',
                    'in_progress': '⚙️ IN PROGRESS',
                    'pending': '⏳ PENDING'
                }
                output += f"\n{status_display.get(status, status)}\n"
                output += "-" * 70 + "\n"
                
                for task in sorted(tasks, key=lambda t: {'high': 0, 'medium': 1, 'low': 2}.get(t.priority, 3)):
                    output += f"  {task}\n"
                    if task.description:
                        output += f"     {task.description}\n"
        
        output += "\n" + "=" * 70 + "\n"
        
        # Show statistics
        stats = self.get_statistics()
        output += f"📊 Statistics: {stats['completed']}/{stats['total']} completed ({stats['completion_rate']})\n"
        output += "=" * 70 + "\n"
        
        return output
    
    def display_task_details(self, task_id: float) -> str:
        """Display detailed view of a task"""
        task = self.get_task(task_id)
        if not task:
            return f"❌ Task not found\n"
        
        output = f"\n📋 TASK DETAILS\n"
        output += "=" * 70 + "\n"
        output += f"Title: {task.title}\n"
        output += f"Status: {task.status}\n"
        output += f"Priority: {task.priority}\n"
        if task.description:
            output += f"Description: {task.description}\n"
        output += f"Created: {task.created_at}\n"
        if task.completed_at:
            output += f"Completed: {task.completed_at}\n"
        output += "=" * 70 + "\n"
        
        return output
    
    def display_statistics(self) -> str:
        """Display task statistics"""
        stats = self.get_statistics()
        
        output = "\n📊 TASK STATISTICS\n"
        output += "=" * 70 + "\n"
        output += f"Total Tasks: {stats['total']}\n"
        output += f"Completed: {stats['completed']}\n"
        output += f"In Progress: {stats['in_progress']}\n"
        output += f"Pending: {stats['pending']}\n"
        output += f"Completion Rate: {stats['completion_rate']}\n"
        output += "=" * 70 + "\n"
        
        return output


def demo():
    """Demonstrate the to-do list"""
    
    print("\n🎯 TO-DO LIST MANAGER DEMO\n")
    
    # Initialize
    todo = TodoListManager()
    
    # Add tasks
    print("➕ Adding sample tasks...")
    todo.add_task("Complete MIKE setup", "high", "Install and configure MIKE AI Agent")
    todo.add_task("Test voice recognition", "medium", "Test voice input functionality")
    todo.add_task("Review documentation", "medium")
    todo.add_task("Fix bugs", "high")
    todo.add_task("Add more applications", "low", "Extend app launcher")
    
    # Display all tasks
    print(todo.display_all_tasks())
    
    # Mark some as completed
    tasks = todo.get_all_tasks()
    if tasks:
        todo.mark_complete(tasks[0].id)
    
    # Display updated view
    print(todo.display_all_tasks())
    
    # Show statistics
    print(todo.display_statistics())
    
    return todo


if __name__ == "__main__":
    demo()
