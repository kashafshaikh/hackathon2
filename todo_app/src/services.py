"""
Business logic services for the Todo Console Application.
Handles all task operations and validations.
"""

from typing import List, Optional
from models import InMemoryStorage, Task


class TaskService:
    """Service layer for task operations."""

    def __init__(self):
        """Initialize the service with in-memory storage."""
        self.storage = InMemoryStorage()

    def add_task(self, title: str, description: str = "") -> str:
        """
        Add a new task.

        Args:
            title: Title of the task (non-empty)
            description: Description of the task (optional)

        Returns:
            Success message or error message if operation fails
        """
        try:
            task = self.storage.add_task(title, description)
            return f"Task #{task.id} added successfully"
        except ValueError as e:
            return f"Error: {str(e)}"

    def view_all_tasks(self) -> str:
        """
        View all tasks with ID and status.

        Returns:
            Formatted string with all tasks or message if no tasks exist
        """
        tasks = self.storage.get_all_tasks()

        if not tasks:
            return "No tasks found."

        # Create formatted output
        output_lines = []
        output_lines.append("ID  | Title              | Description       | Status")
        output_lines.append("----|--------------------|-------------------|---------")

        for task in tasks:
            status = "Completed" if task.is_completed else "Pending"
            # Truncate title and description for display
            title_display = task.title[:18] if len(task.title) <= 18 else task.title[:17] + "."
            desc_display = task.description[:15] if len(task.description) <= 15 else task.description[:14] + "."
            output_lines.append(f"{task.id:<3} | {title_display:<18} | {desc_display:<17} | {status}")

        return "\n".join(output_lines)

    def update_task(self, task_id: int, new_title: str = None, new_description: str = None) -> str:
        """
        Update a task by ID.

        Args:
            task_id: ID of the task to update
            new_title: New title for the task (optional)
            new_description: New description for the task (optional)

        Returns:
            Success or error message
        """
        # Check if both new_title and new_description are None
        if new_title is None and new_description is None:
            return "Error: Please provide at least one field to update (title or description)"

        # Check if task exists
        task = self.storage.get_task(task_id)
        if not task:
            return f"Error: Task with ID {task_id} not found"

        try:
            success = self.storage.update_task(task_id, new_title, new_description)
            if success:
                return f"Task #{task_id} updated successfully"
            else:
                return f"Error: Task with ID {task_id} not found"
        except ValueError as e:
            return f"Error: {str(e)}"

    def delete_task(self, task_id: int) -> str:
        """
        Delete a task by ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            Success or error message
        """
        task = self.storage.get_task(task_id)
        if not task:
            return f"Error: Task with ID {task_id} not found"

        success = self.storage.delete_task(task_id)
        if success:
            return f"Task #{task_id} deleted successfully"
        else:
            return f"Error: Failed to delete task with ID {task_id}"

    def toggle_task_completion(self, task_id: int) -> str:
        """
        Toggle the completion status of a task.

        Args:
            task_id: ID of the task to toggle

        Returns:
            Success or error message
        """
        task = self.storage.get_task(task_id)
        if not task:
            return f"Error: Task with ID {task_id} not found"

        success = self.storage.toggle_task_completion(task_id)
        if success:
            new_status = "completed" if task.is_completed else "incomplete"
            return f"Task #{task_id} marked as {new_status}"
        else:
            return f"Error: Failed to toggle task with ID {task_id}"

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self.storage.get_task(task_id)