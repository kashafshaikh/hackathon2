"""
Data models for the Todo Console Application.
Implements in-memory storage for tasks.
"""

from typing import Dict, List, Optional


class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id: integer (auto-increment)
        title: string (non-empty)
        description: string (can be empty)
        is_completed: boolean (default: False)
    """

    def __init__(self, id: int, title: str, description: str = ""):
        """
        Initialize a new Task.

        Args:
            id: Unique identifier for the task
            title: Title of the task (non-empty)
            description: Description of the task (optional)

        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        self.id = id
        self.title = title.strip()
        self.description = description.strip()
        self.is_completed = False


class InMemoryStorage:
    """
    In-memory storage for tasks using Python dictionaries.
    Implements auto-incrementing ID functionality.
    """

    def __init__(self):
        """Initialize empty storage with next_id counter."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to storage with auto-incremented ID.

        Args:
            title: Title of the task (non-empty)
            description: Description of the task (optional)

        Returns:
            The newly created Task object

        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        task = Task(self._next_id, title, description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks from storage.

        Returns:
            List of all Task objects
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update a task's title and/or description.

        Args:
            task_id: ID of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)

        Returns:
            True if task was updated, False if task not found

        Raises:
            ValueError: If title is provided but is empty or contains only whitespace
        """
        task = self.get_task(task_id)
        if not task:
            return False

        # Validate title if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title.strip()

        # Update description if provided
        if description is not None:
            task.description = description.strip()

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id: ID of the task to toggle

        Returns:
            True if task was toggled, False if task not found
        """
        task = self.get_task(task_id)
        if not task:
            return False

        task.is_completed = not task.is_completed
        return True