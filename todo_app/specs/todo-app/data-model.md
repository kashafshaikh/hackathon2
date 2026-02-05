# Data Model for Todo In-Memory Python Console App

## Entities

### TodoItem
**Description**: Represents a single todo item in the application

**Fields**:
- `id`: int (unique identifier, auto-generated)
- `description`: str (text description of the task)
- `completed`: bool (completion status, default False)
- `priority`: str (priority level - "Low", "Medium", or "High", default "Medium")
- `created_at`: datetime (timestamp when todo was created)
- `updated_at`: datetime (timestamp when todo was last modified)

**Validation Rules**:
- `id` must be unique within the collection
- `description` must not be empty or None
- `priority` must be one of ["Low", "Medium", "High"]
- `completed` must be boolean
- `created_at` and `updated_at` must be valid datetime objects

**State Transitions**:
- Creation: `completed` = False (default)
- Update: `completed` can transition between True/False
- `updated_at` updates whenever the todo is modified

### TodoCollection
**Description**: In-memory storage container for todo items

**Fields**:
- `todos`: dict[int, TodoItem] (dictionary mapping ID to TodoItem objects)
- `next_id`: int (counter for generating unique IDs)

**Operations**:
- Add a TodoItem (generates new ID)
- Retrieve TodoItem by ID
- Update TodoItem by ID
- Delete TodoItem by ID
- List all TodoItems (with optional filters)

**Relationships**:
- Contains zero or more TodoItem instances
- Each TodoItem has exactly one TodoCollection as its parent

## Schema Representation

```python
from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class TodoItem:
    def __init__(self, id: int, description: str, completed: bool = False,
                 priority: Priority = Priority.MEDIUM):
        self.id = id
        self.description = description.strip()
        self.completed = completed
        self.priority = priority
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class TodoCollection:
    def __init__(self):
        self.todos = {}
        self.next_id = 1

    def add(self, description: str, priority: Priority = Priority.MEDIUM) -> TodoItem:
        # Creates and adds a new TodoItem
        pass

    def get(self, id: int) -> TodoItem:
        # Retrieves TodoItem by ID
        pass

    def update(self, id: int, description: str = None, completed: bool = None,
               priority: Priority = None) -> TodoItem:
        # Updates TodoItem properties
        pass

    def delete(self, id: int) -> bool:
        # Removes TodoItem by ID
        pass

    def list_all(self) -> list[TodoItem]:
        # Returns all TodoItems
        pass

    def list_by_status(self, completed: bool) -> list[TodoItem]:
        # Returns TodoItems filtered by completion status
        pass

    def list_by_priority(self, priority: Priority) -> list[TodoItem]:
        # Returns TodoItems filtered by priority
        pass
```