# Phase I – In-Memory Todo Console Application Specification

## 1. Overview

### 1.1 Purpose
Create a console-based todo application in Python that manages tasks in-memory. The application should provide core functionality for managing todo items with a clean, user-friendly command-line interface.

### 1.2 Scope
- In-memory storage of todo items
- Menu-driven console user interface
- Core task operations (Add, View, Update, Delete, Toggle Complete)
- Clear and user-friendly CLI messages
- Robust error handling for all edge cases

### 1.3 Out of Scope
- Persistent storage (database/files)
- Web interface
- Multi-user support
- Priority levels
- Search functionality

## 2. Functional Requirements

### 2.1 Core Operations

#### 2.1.1 Add Task
- **Requirement**: Users can add new tasks with title and description
- **Input**: Task title and description
- **Processing**: Store the task with a unique auto-incrementing ID and default incomplete status
- **Output**: Success message confirming addition with task ID
- **Acceptance Criteria**:
  - [ ] Task is stored in memory with auto-incrementing ID
  - [ ] Title and description are stored
  - [ ] Task status defaults to incomplete
  - [ ] Success message is displayed to user
  - [ ] Empty title validation prevents task creation
  - [ ] User receives appropriate error message for empty title

#### 2.1.2 View All Tasks
- **Requirement**: Display all tasks with ID and status
- **Input**: None (or menu selection)
- **Processing**: Retrieve all tasks from memory and format for display
- **Output**: Formatted list of tasks showing ID, title, description, and completion status
- **Acceptance Criteria**:
  - [ ] All tasks are displayed
  - [ ] ID of each task is shown
  - [ ] Title and description are visible
  - [ ] Completion status is clearly indicated
  - [ ] Format is clean and readable
  - [ ] Appropriate message displayed when no tasks exist
  - [ ] Table format with clear column headers

#### 2.1.3 Update Task
- **Requirement**: Modify an existing task by ID
- **Input**: Task ID and updated information (title or description)
- **Processing**: Update the specified task's properties in memory
- **Output**: Success message confirming update
- **Acceptance Criteria**:
  - [ ] Task properties are updated correctly
  - [ ] Operation is confirmed to user
  - [ ] Invalid IDs are handled with appropriate error message
  - [ ] Empty title validation prevents update to invalid state
  - [ ] User receives appropriate error message for empty title during update
  - [ ] Update operation handles partial updates (title only, description only, or both)

#### 2.1.4 Delete Task
- **Requirement**: Remove a task from the list by ID
- **Input**: Task ID
- **Processing**: Remove the specified task from memory
- **Output**: Success message confirming deletion
- **Acceptance Criteria**:
  - [ ] Task is removed from memory
  - [ ] Operation is confirmed to user
  - [ ] Invalid IDs are handled with appropriate error message
  - [ ] Attempting to delete non-existent task shows appropriate error
  - [ ] Subsequent operations do not reference the deleted task

#### 2.1.5 Toggle Task Completion Status
- **Requirement**: Change a task's completion status (complete/incomplete)
- **Input**: Task ID
- **Processing**: Toggle the completion status of the specified task
- **Output**: Success message confirming status change
- **Acceptance Criteria**:
  - [ ] Task completion status is toggled (complete ↔ incomplete)
  - [ ] Operation is confirmed to user
  - [ ] Invalid IDs are handled with appropriate error message
  - [ ] Attempting to toggle non-existent task shows appropriate error
  - [ ] Status change is immediately reflected in the system

## 3. Non-Functional Requirements

### 3.1 In-Memory Data Storage
- Application must maintain all data in memory only
- No persistent storage (files, databases)
- Data is lost when application exits
- Memory usage should be efficient
- ID auto-increment must be consistent and never duplicate

### 3.2 User Interface Requirements
- **Clear CLI Messages**: All user-facing messages must be clear and helpful
- **Input Validation**: All user inputs must be validated with appropriate error messages
- **Clean Formatting**: Display output must be well-formatted and easy to read
- **Menu-Driven Interface**: Application must provide a clear menu system for navigation
- **User Experience**: Interface should be intuitive and guide users effectively

### 3.3 Performance Requirements
- Response time for all operations should be < 100ms
- Application should handle up to 1000 tasks efficiently
- Menu navigation should be responsive

### 3.4 Error Handling Requirements
- All invalid inputs must be handled gracefully
- Appropriate error messages must be displayed
- Application should not crash under any circumstances
- Recovery from invalid states should be seamless

## 4. Edge Cases and Error Scenarios

### 4.1 Invalid User Inputs
- **Invalid menu choice**: Non-numeric input, out of range numbers (not 1-6)
  - Display: "Error: Invalid choice. Please enter a number between 1-6."
- **Non-existent task IDs**: Operations on IDs that don't exist
  - Display: "Error: Task with ID X not found"
- **Empty titles**: During add/update operations
  - Display: "Error: Title cannot be empty."
- **Invalid numeric input**: When integer is expected but non-numeric entered
  - Display: "Error: Please enter a valid number."

### 4.2 Empty State Handling
- **Empty task list**: When viewing tasks with no tasks
  - Display: "No tasks found."
- **Empty task list**: When attempting update/delete/toggle with no tasks
  - Display: "No tasks available to [operation]."

### 4.3 Boundary Conditions
- **Large ID values**: Handle maximum integer values appropriately
- **Long text inputs**: Handle very long titles/descriptions without crashing
- **Special characters**: Handle Unicode, symbols, and special characters properly

## 5. Data Model

### 5.1 Task Entity
```
Task:
- id: integer (auto-increment, unique)
- title: string (non-empty, trimmed of leading/trailing whitespace)
- description: string (can be empty, trimmed of leading/trailing whitespace)
- is_completed: boolean (default: False)
```

### 5.2 Storage Structure
- In-memory storage using Python dictionaries for O(1) lookup
- Auto-incrementing ID system starting from 1
- Next available ID tracked to ensure uniqueness
- Thread-safe operations (if applicable)

## 6. CLI Flow

### 6.1 Main Menu
The application presents a menu-driven interface that loops until user chooses to exit:

```
Todo Console Application
=======================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Task Completion
6. Exit

Enter your choice (1-6):
```

### 6.2 Operation Flows

#### Add Task Flow
1. User selects "Add Task" from menu
2. System prompts for title: "Enter task title: "
3. System validates title is not empty
4. If empty, shows error and returns to menu
5. If valid, system prompts for description: "Enter task description (optional, press Enter to skip): "
6. System creates new task with auto-incremented ID
7. System displays success message: "Task #X added successfully"
8. System pauses briefly before returning to menu

#### View All Tasks Flow
1. User selects "View All Tasks" from menu
2. System retrieves all tasks from memory
3. If no tasks exist, displays: "No tasks found."
4. If tasks exist, displays formatted table:
   ```
   ID  | Title              | Description       | Status
   ----|--------------------|-------------------|---------
   1   | Sample Task        | Description here  | Pending
   2   | Another Task       | Another desc      | Completed
   ```
5. System pauses briefly before returning to menu

#### Update Task Flow
1. User selects "Update Task" from menu
2. If no tasks exist, displays: "No tasks available to update." and returns to menu
3. System prompts for task ID: "Enter task ID to update: "
4. System validates input is numeric
5. System checks if task exists
6. If task doesn't exist, displays error and returns to menu
7. System prompts for new title: "Enter new title (or press Enter to keep current): "
8. System prompts for new description: "Enter new description (or press Enter to keep current): "
9. System validates that at least one field is provided for update
10. System performs update operation
11. System displays appropriate success/error message
12. System pauses briefly before returning to menu

#### Delete Task Flow
1. User selects "Delete Task" from menu
2. If no tasks exist, displays: "No tasks available to delete." and returns to menu
3. System prompts for task ID: "Enter task ID to delete: "
4. System validates input is numeric
5. System checks if task exists
6. If task doesn't exist, displays error and returns to menu
7. System removes task from memory
8. System displays success message: "Task #X deleted successfully"
9. System pauses briefly before returning to menu

#### Toggle Task Completion Flow
1. User selects "Toggle Task Completion" from menu
2. If no tasks exist, displays: "No tasks available to toggle." and returns to menu
3. System prompts for task ID: "Enter task ID to toggle completion: "
4. System validates input is numeric
5. System checks if task exists
6. If task doesn't exist, displays error and returns to menu
7. System toggles completion status
8. System displays success message: "Task #X marked as [completed/incomplete]"
9. System pauses briefly before returning to menu

#### Exit Flow
1. User selects "Exit" from menu
2. System displays: "Thank you for using the Todo Console Application!"
3. Application terminates gracefully

### 6.3 Message Format
- **Success Messages**: "Task #X [operation] successfully"
- **Error Messages**: "Error: [descriptive error message]"
- **Input Prompts**: "[Descriptive prompt]: "
- **Informational Messages**: "[Informative text]"

### 6.4 User Experience Enhancements
- **Pause after operations**: Brief pause with prompt to "Press Enter to continue..." to allow users to see results
- **Graceful exit**: Handle Ctrl+C and Ctrl+D gracefully with exit message
- **Input sanitization**: Trim whitespace from user inputs automatically

## 7. Technical Constraints

### 7.1 Technology Stack
- Python 3.13+
- Standard library only (no external dependencies)
- Console-based interface

### 7.2 Folder Structure
```
src/
├── main.py        # Main application entry point with menu interface
├── models.py      # Data models and in-memory storage implementation
└── services.py    # Business logic and task operations
```

### 7.3 Code Requirements
- Clean, modular code following PEP 8 standards
- Proper separation of concerns between files
- Adequate documentation and comments
- Type hints for all public interfaces
- Comprehensive error handling

## 8. Acceptance Criteria

### 8.1 Core Functionality
- [ ] Add task feature works correctly with validation
- [ ] View all tasks feature works correctly with proper formatting
- [ ] Update task feature works correctly with validation
- [ ] Delete task feature works correctly with proper cleanup
- [ ] Toggle task completion feature works correctly with status change

### 8.2 Edge Case Handling
- [ ] Empty title validation prevents invalid task creation
- [ ] Non-existent task ID operations handled gracefully
- [ ] Empty task list operations handled gracefully
- [ ] Invalid menu choices handled gracefully
- [ ] Invalid numeric input handled gracefully
- [ ] Special character inputs handled properly

### 8.3 Application Requirements
- [ ] App runs using: `python src/main.py`
- [ ] Menu-driven interface is present and functional
- [ ] All operations provide clear success/error messages
- [ ] No manual code written by the user (all code generated by Claude Code)

### 8.4 Quality Requirements
- [ ] Input validation prevents crashes
- [ ] Error messages are helpful and clear
- [ ] Display formatting is clean and readable
- [ ] ID auto-increment system works correctly
- [ ] Task completion status toggles properly
- [ ] User experience is smooth with appropriate pauses

### 8.5 Data Integrity
- [ ] Tasks persist in memory during application lifetime
- [ ] ID uniqueness is maintained
- [ ] No duplicate IDs are created
- [ ] Deleted tasks are properly removed from storage
- [ ] Updates only affect specified task
- [ ] Toggle only affects specified task's status