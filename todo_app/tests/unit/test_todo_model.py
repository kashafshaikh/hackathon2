"""
Unit tests for the todo model.
"""

import pytest
from datetime import datetime
from src.models.todo_model import TodoItem, TodoCollection, Priority


class TestTodoItem:
    """Test cases for the TodoItem class."""

    def test_create_todo_item(self):
        """Test creating a new TodoItem."""
        todo = TodoItem(1, "Test description")

        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is False
        assert todo.priority == Priority.MEDIUM
        assert isinstance(todo.created_at, datetime)
        assert isinstance(todo.updated_at, datetime)

    def test_create_todo_item_with_priority(self):
        """Test creating a TodoItem with specific priority."""
        todo = TodoItem(1, "Test description", priority=Priority.HIGH)

        assert todo.priority == Priority.HIGH

    def test_mark_completed(self):
        """Test marking a todo item as completed."""
        todo = TodoItem(1, "Test description")
        initial_updated_at = todo.updated_at

        todo.mark_completed()

        assert todo.completed is True
        assert todo.updated_at > initial_updated_at

    def test_update_description(self):
        """Test updating a todo item's description."""
        todo = TodoItem(1, "Original description")
        initial_updated_at = todo.updated_at

        todo.update_description("New description")

        assert todo.description == "New description"
        assert todo.updated_at > initial_updated_at

    def test_update_description_empty(self):
        """Test updating a todo item's description with empty string raises ValueError."""
        todo = TodoItem(1, "Original description")

        with pytest.raises(ValueError):
            todo.update_description("")

    def test_update_priority(self):
        """Test updating a todo item's priority."""
        todo = TodoItem(1, "Test description")
        initial_updated_at = todo.updated_at

        todo.update_priority(Priority.LOW)

        assert todo.priority == Priority.LOW
        assert todo.updated_at > initial_updated_at


class TestTodoCollection:
    """Test cases for the TodoCollection class."""

    def test_initial_state(self):
        """Test initial state of TodoCollection."""
        collection = TodoCollection()

        assert len(collection.todos) == 0
        assert collection.next_id == 1

    def test_add_todo(self):
        """Test adding a new todo to the collection."""
        collection = TodoCollection()

        todo = collection.add("Test description")

        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.id in collection.todos
        assert collection.next_id == 2

    def test_add_todo_with_priority(self):
        """Test adding a todo with specific priority."""
        collection = TodoCollection()

        todo = collection.add("Test description", Priority.HIGH)

        assert todo.priority == Priority.HIGH

    def test_get_existing_todo(self):
        """Test getting an existing todo by ID."""
        collection = TodoCollection()
        added_todo = collection.add("Test description")

        retrieved_todo = collection.get(added_todo.id)

        assert retrieved_todo is not None
        assert retrieved_todo.id == added_todo.id
        assert retrieved_todo.description == added_todo.description

    def test_get_nonexistent_todo(self):
        """Test getting a nonexistent todo returns None."""
        collection = TodoCollection()

        result = collection.get(999)

        assert result is None

    def test_update_todo_description(self):
        """Test updating a todo's description."""
        collection = TodoCollection()
        added_todo = collection.add("Original description")

        updated_todo = collection.update(added_todo.id, description="New description")

        assert updated_todo is not None
        assert updated_todo.description == "New description"

    def test_update_todo_completion(self):
        """Test updating a todo's completion status."""
        collection = TodoCollection()
        added_todo = collection.add("Test description")

        updated_todo = collection.update(added_todo.id, completed=True)

        assert updated_todo is not None
        assert updated_todo.completed is True

    def test_update_todo_priority(self):
        """Test updating a todo's priority."""
        collection = TodoCollection()
        added_todo = collection.add("Test description")

        updated_todo = collection.update(added_todo.id, priority=Priority.HIGH)

        assert updated_todo is not None
        assert updated_todo.priority == Priority.HIGH

    def test_update_nonexistent_todo(self):
        """Test updating a nonexistent todo returns None."""
        collection = TodoCollection()

        result = collection.update(999, description="New description")

        assert result is None

    def test_delete_existing_todo(self):
        """Test deleting an existing todo."""
        collection = TodoCollection()
        added_todo = collection.add("Test description")

        result = collection.delete(added_todo.id)

        assert result is True
        assert added_todo.id not in collection.todos

    def test_delete_nonexistent_todo(self):
        """Test deleting a nonexistent todo returns False."""
        collection = TodoCollection()

        result = collection.delete(999)

        assert result is False

    def test_list_all_todos(self):
        """Test listing all todos."""
        collection = TodoCollection()
        todo1 = collection.add("First task")
        todo2 = collection.add("Second task")

        todos = collection.list_all()

        assert len(todos) == 2
        ids = [todo.id for todo in todos]
        assert todo1.id in ids
        assert todo2.id in ids

    def test_list_by_status(self):
        """Test listing todos by completion status."""
        collection = TodoCollection()
        pending_todo = collection.add("Pending task")
        completed_todo = collection.add("Completed task")
        collection.update(completed_todo.id, completed=True)

        pending_todos = collection.list_by_status(False)
        completed_todos = collection.list_by_status(True)

        assert len(pending_todos) == 1
        assert pending_todos[0].id == pending_todo.id
        assert len(completed_todos) == 1
        assert completed_todos[0].id == completed_todo.id

    def test_list_by_priority(self):
        """Test listing todos by priority."""
        collection = TodoCollection()
        medium_todo = collection.add("Medium priority task")
        high_todo = collection.add("High priority task", Priority.HIGH)

        medium_todos = collection.list_by_priority(Priority.MEDIUM)
        high_todos = collection.list_by_priority(Priority.HIGH)

        assert len(medium_todos) == 1
        assert medium_todos[0].id == medium_todo.id
        assert len(high_todos) == 1
        assert high_todos[0].id == high_todo.id

    def test_search_todos(self):
        """Test searching todos by keyword."""
        collection = TodoCollection()
        matching_todo = collection.add("Buy groceries for the week")
        non_matching_todo = collection.add("Call the doctor")

        results = collection.search("groceries")

        assert len(results) == 1
        assert results[0].id == matching_todo.id

    def test_search_todos_case_insensitive(self):
        """Test that search is case-insensitive."""
        collection = TodoCollection()
        matching_todo = collection.add("Buy groceries for the week")

        results = collection.search("GROCERIES")

        assert len(results) == 1
        assert results[0].id == matching_todo.id