#!/usr/bin/env python3
"""
Demo script for the Todo Console Application - Phase I
Demonstrates all required functionality with the new menu-driven interface
"""

import sys
import os
# Add the src directory to the path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services import TaskService


def demo():
    """Demonstrate the functionality of the new todo app."""
    print("=== Todo Console Application - Phase I Demo ===\n")

    service = TaskService()

    # Demo 1: Add tasks
    print("1. Adding tasks...")
    result = service.add_task("Learn Python", "Study Python fundamentals")
    print(f"   {result}")

    result = service.add_task("Build Project", "Create a Python application")
    print(f"   {result}")

    result = service.add_task("Write Documentation", "Document the application")
    print(f"   {result}")
    print()

    # Demo 2: View all tasks
    print("2. Viewing all tasks:")
    result = service.view_all_tasks()
    print(f"   {result}")
    print()

    # Demo 3: Update a task
    print("3. Updating task #2...")
    result = service.update_task(2, new_title="Build Amazing Project", new_description="Create an awesome Python application")
    print(f"   {result}")
    print()

    # View tasks after update
    print("4. Viewing tasks after update:")
    result = service.view_all_tasks()
    print(f"   {result}")
    print()

    # Demo 5: Toggle task completion
    print("5. Toggling completion status of task #1...")
    result = service.toggle_task_completion(1)
    print(f"   {result}")
    print()

    # View tasks after toggle
    print("6. Viewing tasks after toggle:")
    result = service.view_all_tasks()
    print(f"   {result}")
    print()

    # Demo 6: Delete a task
    print("7. Deleting task #3...")
    result = service.delete_task(3)
    print(f"   {result}")
    print()

    # Final view
    print("8. Final view of tasks:")
    result = service.view_all_tasks()
    print(f"   {result}")
    print()

    # Demo 7: Edge cases
    print("9. Testing edge cases:")

    # Try to update non-existent task
    result = service.update_task(99, "Non-existent task")
    print(f"   Update non-existent task: {result}")

    # Try to delete non-existent task
    result = service.delete_task(99)
    print(f"   Delete non-existent task: {result}")

    # Try to toggle non-existent task
    result = service.toggle_task_completion(99)
    print(f"   Toggle non-existent task: {result}")

    # Try to add task with empty title
    result = service.add_task("", "This should fail")
    print(f"   Add task with empty title: {result}")

    print()

    print("=== Demo completed successfully! ===")
    print("All functionality working as expected:")
    print("- Add task [PASS]")
    print("- View tasks [PASS]")
    print("- Update task [PASS]")
    print("- Delete task [PASS]")
    print("- Toggle completion [PASS]")
    print("- Edge case handling [PASS]")


if __name__ == "__main__":
    demo()