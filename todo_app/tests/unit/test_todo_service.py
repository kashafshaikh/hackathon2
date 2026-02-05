"""
Unit tests for the todo service.
"""

import pytest
from src.services.todo_service import TodoService, Priority


class TestTodoService:
    """Test cases for the TodoService class."""

    def test_initial_state(self):
        """Test initial state of TodoService."""
        service = TodoService()

        assert len(service.collection.list_all()) == 0

    def test_add_todo(self):
        """Test adding a new todo."""
        service = TodoService()

        todo = service.add_todo("Test description")

        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is False
        assert todo.priority == Priority.MEDIUM

    def test_add_todo_with_priority(self):
        """Test adding a todo with specific priority."""
        service = TodoService()

        todo = service.add_todo("Test description", Priority.HIGH)

        assert todo.priority == Priority.HIGH

    def test_list_todos(self):
        """Test listing all todos."""
        service = TodoService()
        service.add_todo("First task")
        service.add_todo("Second task")

        todos = service.list_todos()

        assert len(todos) == 2

    def test_list_todos_by_status(self):
        """Test listing todos by status."""
        service = TodoService()
        pending_todo = service.add_todo("Pending task")
        completed_todo = service.add_todo("Completed task")
        service.complete_todo(completed_todo.id)

        pending_todos = service.list_todos_by_status(False)
        completed_todos = service.list_todos_by_status(True)

        assert len(pending_todos) == 1
        assert pending_todos[0].id == pending_todo.id
        assert len(completed_todos) == 1
        assert completed_todos[0].id == completed_todo.id

    def test_complete_todo(self):
        """Test completing a todo."""
        service = TodoService()
        todo = service.add_todo("Test task")

        result = service.complete_todo(todo.id)

        assert result is True
        updated_todo = service.get_todo(todo.id)
        assert updated_todo is not None
        assert updated_todo.completed is True

    def test_complete_nonexistent_todo(self):
        """Test completing a nonexistent todo."""
        service = TodoService()

        result = service.complete_todo(999)

        assert result is False

    def test_delete_todo(self):
        """Test deleting a todo."""
        service = TodoService()
        todo = service.add_todo("Test task")

        result = service.delete_todo(todo.id)

        assert result is True
        assert service.get_todo(todo.id) is None

    def test_delete_nonexistent_todo(self):
        """Test deleting a nonexistent todo."""
        service = TodoService()

        result = service.delete_todo(999)

        assert result is False

    def test_update_todo_description(self):
        """Test updating a todo's description."""
        service = TodoService()
        todo = service.add_todo("Original description")

        result = service.update_todo(todo.id, description="New description")

        assert result is True
        updated_todo = service.get_todo(todo.id)
        assert updated_todo is not None
        assert updated_todo.description == "New description"

    def test_update_todo_priority(self):
        """Test updating a todo's priority."""
        service = TodoService()
        todo = service.add_todo("Test description")

        result = service.update_todo(todo.id, priority=Priority.HIGH)

        assert result is True
        updated_todo = service.get_todo(todo.id)
        assert updated_todo is not None
        assert updated_todo.priority == Priority.HIGH

    def test_update_nonexistent_todo(self):
        """Test updating a nonexistent todo."""
        service = TodoService()

        result = service.update_todo(999, description="New description")

        assert result is False

    def test_search_todos(self):
        """Test searching todos by keyword."""
        service = TodoService()
        matching_todo = service.add_todo("Buy groceries for the week")
        non_matching_todo = service.add_todo("Call the doctor")

        results = service.search_todos("groceries")

        assert len(results) == 1
        assert results[0].id == matching_todo.id

    def test_search_todos_case_insensitive(self):
        """Test that search is case-insensitive."""
        service = TodoService()
        matching_todo = service.add_todo("Buy groceries for the week")

        results = service.search_todos("GROCERIES")

        assert len(results) == 1
        assert results[0].id == matching_todo.id

    def test_get_todo(self):
        """Test getting a specific todo by ID."""
        service = TodoService()
        todo = service.add_todo("Test task")

        retrieved = service.get_todo(todo.id)

        assert retrieved is not None
        assert retrieved.id == todo.id
        assert retrieved.description == todo.description

    def test_get_nonexistent_todo(self):
        """Test getting a nonexistent todo."""
        service = TodoService()

        result = service.get_todo(999)

        assert result is None