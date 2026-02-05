# Implementation Plan: Todo Console Application

## Overview
Detailed plan for implementing a menu-driven Todo Console Application with in-memory storage, following the specification requirements.

## Architecture Overview
The application follows a layered architecture with clear separation of concerns:
- **Presentation Layer** (main.py): Menu interface and user interaction
- **Service Layer** (services.py): Business logic and operations coordination
- **Model Layer** (models.py): Data structures and in-memory storage

## File-by-File Responsibilities

### 1. models.py - Data Models and Storage Layer
**Purpose**: Defines the data structures and implements in-memory storage.

#### Classes and Functions:

**Class: Task**
- **Attributes**:
  - `id`: integer (auto-increment)
  - `title`: string (non-empty)
  - `description`: string (can be empty)
  - `is_completed`: boolean (default: False)
- **Constructor**: `__init__(self, id: int, title: str, description: str = "")`
  - Validates that title is not empty
  - Strips leading/trailing whitespace
  - Initializes `is_completed` to False

**Class: InMemoryStorage**
- **Private Attributes**:
  - `self._tasks`: Dict[int, Task] - Dictionary storing tasks by ID
  - `self._next_id`: int - Counter for next available ID (starts at 1)

- **Methods**:
  - `__init__(self)`: Initializes empty storage with `_next_id = 1`
  - `add_task(self, title: str, description: str = "") -> Task`:
    - Creates new Task with current `_next_id`
    - Stores task in `_tasks` dictionary
    - Increments `_next_id`
    - Returns the created Task
  - `get_task(self, task_id: int) -> Optional[Task]`:
    - Returns task if exists, None otherwise
  - `get_all_tasks(self) -> List[Task]`:
    - Returns list of all tasks in storage
  - `update_task(self, task_id: int, title: str = None, description: str = None) -> bool`:
    - Updates task if exists and returns True
    - Validates title is not empty if provided
    - Returns False if task doesn't exist
  - `delete_task(self, task_id: int) -> bool`:
    - Removes task if exists and returns True
    - Returns False if task doesn't exist
  - `toggle_task_completion(self, task_id: int) -> bool`:
    - Toggles completion status if task exists and returns True
    - Returns False if task doesn't exist

### 2. services.py - Business Logic Layer
**Purpose**: Implements business logic and provides service methods for the application.

#### Classes and Functions:

**Class: TaskService**
- **Attributes**:
  - `storage`: InMemoryStorage instance

- **Methods**:
  - `__init__(self)`: Initializes with new InMemoryStorage instance
  - `add_task(self, title: str, description: str = "") -> str`:
    - Calls storage.add_task
    - Returns success message or error message
  - `view_all_tasks(self) -> str`:
    - Gets all tasks from storage
    - Formats as table with headers: ID, Title, Description, Status
    - Returns "No tasks found." if no tasks exist
  - `update_task(self, task_id: int, new_title: str = None, new_description: str = None) -> str`:
    - Validates that at least one field is provided
    - Checks if task exists
    - Calls storage.update_task
    - Returns success or appropriate error message
  - `delete_task(self, task_id: int) -> str`:
    - Checks if task exists
    - Calls storage.delete_task
    - Returns success or appropriate error message
  - `toggle_task_completion(self, task_id: int) -> str`:
    - Checks if task exists
    - Calls storage.toggle_task_completion
    - Returns success or appropriate error message
  - `get_task_by_id(self, task_id: int) -> Optional[Task]`:
    - Helper method to retrieve a specific task

### 3. main.py - Presentation Layer
**Purpose**: Implements menu-driven interface and user interaction.

#### Functions:

- `get_user_input(prompt: str) -> str`:
  - Handles user input with error handling
  - Catches KeyboardInterrupt and EOFError to exit gracefully

- `get_integer_input(prompt: str) -> int`:
  - Gets integer input with validation
  - Re-prompts on invalid input
  - Handles non-numeric input gracefully

- `display_menu()`:
  - Prints the main menu with options 1-6:
    1. Add Task
    2. View All Tasks
    3. Update Task
    4. Delete Task
    5. Toggle Task Completion
    6. Exit

- `main()`:
  - Main application loop
  - Initializes TaskService
  - Displays menu continuously until user exits
  - Processes user choices with appropriate error handling
  - Each operation shows result before returning to menu

## CLI Control Flow

### Main Application Loop
1. Initialize TaskService
2. Loop indefinitely until user selects "Exit":
   a. Display menu
   b. Get user choice
   c. Process choice (1-6)
   d. Show result
   e. Wait for user to continue
3. Exit gracefully when option 6 selected

### Individual Operation Flows

#### Add Task Flow (Choice 1)
1. Prompt for title
2. Validate title is not empty
3. If empty, show error and return to menu
4. Prompt for description (optional)
5. Call service.add_task()
6. Display result
7. Wait for user to continue

#### View All Tasks Flow (Choice 2)
1. Call service.view_all_tasks()
2. Display result (formatted table or "No tasks found")
3. Wait for user to continue

#### Update Task Flow (Choice 3)
1. Check if any tasks exist, show message if none
2. Prompt for task ID (validate integer)
3. Prompt for new title (optional)
4. Prompt for new description (optional)
5. Validate at least one field provided
6. Call service.update_task()
7. Display result
8. Wait for user to continue

#### Delete Task Flow (Choice 4)
1. Check if any tasks exist, show message if none
2. Prompt for task ID (validate integer)
3. Call service.delete_task()
4. Display result
5. Wait for user to continue

#### Toggle Completion Flow (Choice 5)
1. Check if any tasks exist, show message if none
2. Prompt for task ID (validate integer)
3. Call service.toggle_task_completion()
4. Display result
5. Wait for user to continue

#### Exit Flow (Choice 6)
1. Show goodbye message
2. Break main loop
3. Application terminates

## In-Memory Storage Implementation

### Task Storage Mechanism
- Uses Python dictionary: `{task_id: Task_object}`
- Auto-incrementing ID system starting from 1
- ID uniqueness guaranteed by sequential assignment
- Thread-safe for single-threaded access

### Data Persistence During Runtime
- All data stored in memory within InMemoryStorage instance
- Data survives throughout application lifecycle
- Data lost upon application exit (as specified)
- Efficient O(1) lookup time for operations

## User Input Processing

### Input Sanitization
- All string inputs stripped of leading/trailing whitespace
- Integer inputs validated with retry mechanism
- Empty title validation prevents invalid task creation
- Special characters handled safely

### Error Handling Strategy
- Input validation at each step
- Clear, descriptive error messages
- Graceful recovery from invalid inputs
- No application crashes for any input scenario

### Validation Rules
- Titles must not be empty or whitespace-only
- Task IDs must exist in storage before operations
- Integer inputs must be valid numbers
- At least one field must be provided for update operations

## Error Message Formats

### Success Messages
- Add: "Task #[ID] added successfully"
- Update: "Task #[ID] updated successfully"
- Delete: "Task #[ID] deleted successfully"
- Toggle: "Task #[ID] marked as [completed/incomplete]"

### Error Messages
- General: "Error: [descriptive message]"
- Missing task: "Error: Task with ID [X] not found"
- Empty title: "Error: Title cannot be empty"
- Invalid choice: "Error: Invalid choice. Please enter a number between 1-6."
- Invalid input: "Error: Please enter a valid number."

## Implementation Sequence

1. **Step 1**: Implement models.py with Task and InMemoryStorage classes
2. **Step 2**: Implement services.py with TaskService class
3. **Step 3**: Implement main.py with menu interface and control flow
4. **Step 4**: Test individual components in isolation
5. **Step 5**: Integrate and test full application flow
6. **Step 6**: Verify all edge cases and error conditions
7. **Step 7**: Test with various input scenarios and boundary conditions

## Quality Assurance Points

- All public methods should have type hints
- All user-facing messages should be clear and helpful
- All operations should handle errors gracefully
- Storage should maintain data integrity throughout operations
- Memory usage should be efficient and scale appropriately