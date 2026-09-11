#!/usr/bin/env python3
"""
To-Do List Manager Examples
Demonstrates task management functionality
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.todo_list import TodoListManager, TaskPriority, TaskStatus


def example_1_basic_tasks():
    """Example 1: Create and display tasks"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Task Management")
    print("="*70)
    
    # Create manager
    todo = TodoListManager()
    
    # Add tasks
    print("\nAdding tasks...")
    todo.add_task("Learn Python", "high", "Complete Python fundamentals course")
    todo.add_task("Build a project", "high", "Create a real-world application")
    todo.add_task("Read documentation", "medium", "Study library documentation")
    todo.add_task("Drink water", "low", "Stay hydrated")
    
    # Display all tasks
    print(todo.display_all_tasks())


def example_2_task_operations():
    """Example 2: Update and complete tasks"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Task Operations")
    print("="*70)
    
    todo = TodoListManager()
    
    # Add tasks
    task1 = todo.add_task("Task 1", "high")
    task2 = todo.add_task("Task 2", "medium")
    task3 = todo.add_task("Task 3", "low")
    
    print("\nInitial tasks:")
    print(todo.display_all_tasks())
    
    # Mark task as in progress
    print("Marking Task 1 as in progress...")
    todo.mark_in_progress(task1.id)
    
    # Mark task as complete
    print("Marking Task 2 as complete...")
    todo.mark_complete(task2.id)
    
    print("\nUpdated tasks:")
    print(todo.display_all_tasks())


def example_3_filter_tasks():
    """Example 3: Filter tasks by status and priority"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Filter Tasks")
    print("="*70)
    
    todo = TodoListManager()
    
    # Add various tasks
    todo.add_task("High Priority Task 1", "high")
    todo.add_task("High Priority Task 2", "high")
    todo.add_task("Medium Priority Task", "medium")
    todo.add_task("Low Priority Task", "low")
    
    # Filter by priority
    print("\n🔴 High Priority Tasks:")
    high_tasks = todo.get_tasks_by_priority("high")
    for task in high_tasks:
        print(f"  - {task}")
    
    print("\n🟡 Medium Priority Tasks:")
    medium_tasks = todo.get_tasks_by_priority("medium")
    for task in medium_tasks:
        print(f"  - {task}")
    
    print("\n🟢 Low Priority Tasks:")
    low_tasks = todo.get_tasks_by_priority("low")
    for task in low_tasks:
        print(f"  - {task}")


def example_4_statistics():
    """Example 4: Task statistics"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Task Statistics")
    print("="*70)
    
    todo = TodoListManager()
    
    # Add and update tasks
    print("\nCreating sample tasks...")
    tasks = []
    for i in range(5):
        task = todo.add_task(f"Task {i+1}", ["high", "medium", "low"][i % 3])
        tasks.append(task)
    
    # Mark some as complete
    todo.mark_complete(tasks[0].id)
    todo.mark_complete(tasks[1].id)
    todo.mark_in_progress(tasks[2].id)
    
    # Display statistics
    print(todo.display_statistics())
    
    # Display detailed view
    print(todo.display_all_tasks())


def example_5_delete_tasks():
    """Example 5: Delete tasks"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Delete Tasks")
    print("="*70)
    
    todo = TodoListManager()
    
    # Add tasks
    print("\nAdding tasks...")
    task1 = todo.add_task("Task to keep", "high")
    task2 = todo.add_task("Task to delete", "low")
    task3 = todo.add_task("Another task", "medium")
    
    print(todo.display_all_tasks())
    
    # Delete task
    print("Deleting 'Task to delete'...")
    todo.delete_task(task2.id)
    
    print("\nAfter deletion:")
    print(todo.display_all_tasks())


def example_6_programmatic_use():
    """Example 6: Using TodoListManager in your code"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Programmatic Usage")
    print("="*70)
    
    from src.todo_list import Task, TaskStatus
    
    todo = TodoListManager()
    
    # Create tasks
    task = todo.add_task("Important task", "high", "This is very important")
    
    # Access task properties
    print(f"\nTask ID: {task.id}")
    print(f"Title: {task.title}")
    print(f"Priority: {task.priority}")
    print(f"Status: {task.status}")
    print(f"Created: {task.created_at}")
    
    # Get specific task
    retrieved = todo.get_task(task.id)
    print(f"\nRetrieved: {retrieved}")
    
    # Update task
    todo.update_task(task.id, priority="medium", status=TaskStatus.IN_PROGRESS.value)
    updated = todo.get_task(task.id)
    print(f"Updated: {updated}")
    
    # Get all tasks
    all_tasks = todo.get_all_tasks()
    print(f"\nTotal tasks: {len(all_tasks)}")


def main():
    """
    Run all examples
    """
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#" + "  TO-DO LIST MANAGER - PROGRAMMING EXAMPLES  ".center(68) + "#")
    print("#" + " "*68 + "#")
    print("#"*70)
    
    examples = [
        ("1", "Basic Task Management", example_1_basic_tasks),
        ("2", "Task Operations", example_2_task_operations),
        ("3", "Filter Tasks", example_3_filter_tasks),
        ("4", "Task Statistics", example_4_statistics),
        ("5", "Delete Tasks", example_5_delete_tasks),
        ("6", "Programmatic Usage", example_6_programmatic_use),
        ("7", "Run All Examples", None),
    ]
    
    while True:
        print("\n" + "="*70)
        print("SELECT AN EXAMPLE:")
        print("="*70)
        
        for num, title, _ in examples:
            print(f"  [{num}] {title}")
        print("  [0] Exit")
        
        choice = input("\nEnter choice [0-7]: ").strip()
        
        if choice == '0':
            print("\n👋 Goodbye!\n")
            break
        elif choice == '7':
            # Run all examples
            for num, title, func in examples[:-1]:
                if func:
                    func()
                    input("\nPress Enter for next example...")
        else:
            # Run selected example
            for num, title, func in examples:
                if num == choice and func:
                    func()
                    break
            else:
                print("❌ Invalid option")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
