# Feature Specification: Phase I – Todo Console Application

**Feature Branch**: `feature/todo-app-phase1`
**Created**: 2025-12-07
**Status**: Draft
**Input**: User description: "/sp.specify

Title: Phase I – Todo Console Application Specification
Create a clean, beautiful, professional spec that defines:

- Functional Requirements
- Non-Functional Requirements
- Data Models
- CLI Menu Flow
- Expected Folder Structure
- User Input Validation
- System Behaviour for each action
- Acceptance Criteria
- Error Handling Rules

Use highly structured formatting.
Make it clear and perfect for implementation."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task (Priority: P1)

Users can add new todo items to their list by providing a description.

**Why this priority**: Essential core functionality for any todo application. Without adding tasks, other features are irrelevant.

**Independent Test**: A user can launch the application, add a new todo item (e.g., "Buy groceries"), and then view the list to confirm the item is present.

**Acceptance Scenarios**:

1.  **Given** the application is running, **When** the user selects "Add Task" and enters "Buy groceries", **Then** "Buy groceries" appears in the todo list with a unique ID and "pending" status.
2.  **Given** the application is running, **When** the user selects "Add Task" and enters an empty description, **Then** an error message is displayed, and no task is added.

---

### User Story 2 - View Tasks (Priority: P1)

Users can view a list of all existing todo items, including their unique ID, description, and status.

**Why this priority**: Essential core functionality to see the current state of tasks.

**Independent Test**: A user can add multiple todo items, and then select "View Tasks" to see all added tasks displayed correctly with their status.

**Acceptance Scenarios**:

1.  **Given** the application is running with tasks "Buy groceries" (pending) and "Clean house" (pending), **When** the user selects "View Tasks", **Then** both tasks are displayed with their respective IDs and status.
2.  **Given** the application is running with no tasks, **When** the user selects "View Tasks", **Then** a message indicating no tasks are present is displayed.

---

### User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

Users can change the status of an existing todo item between "pending" and "completed" using its unique ID.

**Why this priority**: Important functionality for managing task progress.

**Independent Test**: A user can add a task, view it, then mark it complete. Viewing the list again should show the task as "completed". Subsequently, they can mark it incomplete, and viewing the list should reflect the change.

**Acceptance Scenarios**:

1.  **Given** the application is running with task ID 1 as "Buy groceries" (pending), **When** the user selects "Mark Task Complete" and enters ID 1, **Then** task ID 1's status changes to "completed".
2.  **Given** the application is running with task ID 2 as "Clean house" (completed), **When** the user selects "Mark Task Incomplete" and enters ID 2, **Then** task ID 2's status changes to "pending".
3.  **Given** the application is running, **When** the user selects "Mark Task Complete/Incomplete" and enters a non-existent ID (e.g., 999), **Then** an error message "Error: Task with ID 999 not found." is displayed.
4.  **Given** the application is running with task ID 1 as "Buy groceries" (completed), **When** the user selects "Mark Task Complete" and enters ID 1, **Then** an informative message "Task with ID 1 is already completed." is displayed, and the status remains unchanged.
5.  **Given** the application is running with task ID 2 as "Clean house" (pending), **When** the user selects "Mark Task Incomplete" and enters ID 2, **Then** an informative message "Task with ID 2 is already pending." is displayed, and the status remains unchanged.

---

### User Story 4 - Update Task (Priority: P2)

Users can modify the description of an existing todo item using its unique ID.

**Why this priority**: Allows for correction and refinement of task descriptions.

**Independent Test**: A user can add a task, view it, then update its description. Viewing the list again should show the updated description.

**Acceptance Scenarios**:

1.  **Given** the application is running with task ID 1 as "Buy groceries", **When** the user selects "Update Task", enters ID 1, and new description "Buy milk and bread", **Then** task ID 1's description changes to "Buy milk and bread".
2.  **Given** the application is running, **When** the user selects "Update Task" and enters a non-existent ID (e.g., 999), **Then** an error message "Error: Task with ID 999 not found." is displayed.
3.  **Given** the application is running, **When** the user selects "Update Task" and enters a non-positive integer ID (e.g., -1), **Then** an error message "Invalid input. Please enter a positive number." is displayed.

---

### User Story 5 - Delete Task (Priority: P3)

Users can remove an existing todo item from the list using its unique ID.

**Why this priority**: Essential for clearing completed or irrelevant tasks, but less critical than adding or viewing.

**Independent Test**: A user can add a task, view it, then delete it. Viewing the list again should show the task is no longer present.

**Acceptance Scenarios**:

1.  **Given** the application is running with task ID 1 as "Buy groceries", **When** the user selects "Delete Task" and enters ID 1, **Then** task ID 1 is removed from the list.
2.  **Given** the application is running, **When** the user selects "Delete Task" and enters a non-existent ID (e.g., 999), **Then** an error message "Error: Task with ID 999 not found." is displayed.
3.  **Given** the application is running, **When** the user selects "Delete Task" and enters a non-positive integer ID (e.g., -1), **Then** an error message "Invalid input. Please enter a positive number." is displayed.

---

### Edge Cases

-   What happens when the user enters non-integer or non-positive integer input for task IDs? The system should display an error and prompt for valid input.
-   How does the system handle an empty list of tasks when attempting to view, update, complete, or delete? Appropriate messages (e.g., "No tasks to display", "List is empty") should be shown.
-   What if a new task description is empty during an update operation? The system should disallow empty descriptions.
-   What happens if a user tries to mark an already completed task as complete? An informative message should be displayed, and the status should remain unchanged.
-   What happens if a user tries to mark an already pending task as incomplete? An informative message should be displayed, and the status should remain unchanged.

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: System MUST provide clear console interface for user interactions (Principle: User-Centric Design).
-   **FR-002**: System MUST validate all user inputs to prevent errors and ensure data integrity (Principle: Error Handling).
-   **FR-003**: System MUST allow users to add, view, mark as complete/incomplete, update, and delete todo items.
-   **FR-004**: System MUST store todo items in-memory for the duration of the application's runtime.
-   **FR-005**: System MUST assign a unique, auto-incrementing integer ID to each new todo item.
-   **FR-006**: System MUST represent a todo item with at least an ID, description, and status (pending/completed).
-   **FR-007**: System MUST provide a main menu with options for all supported actions (add, view, update, complete, delete, exit).

### Non-Functional Requirements

-   **NFR-001 (Performance)**: The application MUST respond to user input within 100ms for all operations.
-   **NFR-002 (Reliability)**: The application MUST gracefully handle invalid user inputs, displaying informative error messages without crashing.
-   **NFR-003 (Maintainability)**: The codebase MUST adhere to the Modularity, Clean Code, and Test-Driven Development principles outlined in the project constitution.
-   **NFR-004 (Usability)**: The CLI menu and prompts MUST be intuitive and easy to navigate for first-time users.

### Data Models

-   **Todo Item**:
    -   `id`: Integer, unique, auto-incrementing identifier.
    -   `description`: String, non-empty, represents the task content.
    -   `status`: String, one of "pending" or "completed", defaults to "pending".

### CLI Menu Flow

1.  **Main Menu**: Displays options: `[1] Add Task`, `[2] View Tasks`, `[3] Update Task`, `[4] Mark Complete`, `[5] Delete Task`, `[6] Exit`.
2.  **User Input**: Prompts the user to enter a choice (1-6).
3.  **Action Execution**: Based on valid input, performs the corresponding action.
4.  **Error Handling**: If invalid input (non-integer, out of range), displays an appropriate error message and returns to Main Menu.
5.  **Loop**: After each action (or error), the Main Menu is redisplayed, continuing until "Exit" is chosen.
6.  **Exit**: The application terminates gracefully when "Exit" is chosen.

### Expected Folder Structure

As per the project constitution, the application will adhere to the following clean folder structure:
-   `/src/models.py`: Contains the `TodoItem` data model.
-   `/src/services.py`: Contains the `TodoService` logic for managing todo items.
-   `/src/main.py`: Contains the main application logic, CLI menu, and user interaction.
-   `/tests/`: Contains unit and integration tests.

### User Input Validation

-   All numerical inputs (e.g., Task ID, menu choice) MUST be validated to ensure they are positive integers. Non-integer or non-positive integer inputs will result in an error message.
-   Task descriptions (for add and update operations) MUST be validated to ensure they are not empty. Empty inputs will result in an error message.
-   Task IDs provided for update, complete, or delete operations MUST correspond to an existing task. Non-existent IDs will result in an "Error: Task with ID [ID] not found." error message.

### System Behaviour for each action

-   **Add Task**:
    -   Prompts user for task description.
    -   Validates description (non-empty).
    -   Creates `TodoItem` with new auto-incremented ID and "pending" status.
    -   Adds to in-memory list.
    -   Confirms addition to user.
-   **View Tasks**:
    -   Displays all tasks with ID, description, and status.
    -   If no tasks, displays "No tasks to display."
-   **Update Task**:
    -   Prompts for Task ID and new description.
    -   Validates ID (integer, positive, exists) and description (non-empty).
    -   Updates the task's description.
    -   Confirms update to user.
-   **Mark Complete/Incomplete**:
    -   Prompts user to choose 'complete' or 'incomplete' and for Task ID.
    -   Validates ID (integer, positive, exists).
    -   If marking complete: Sets task status to "completed" if currently "pending". Informs user if already "completed".
    -   If marking incomplete: Sets task status to "pending" if currently "completed". Informs user if already "pending".
    -   Confirms status change or provides informative message to user.
-   **Delete Task**:
    -   Prompts for Task ID.
    -   Validates ID (integer, positive, exists).
    -   Removes task from in-memory list.
    -   Confirms deletion to user.
-   **Exit**:
    -   Terminates the application.

### Error Handling Rules

-   **Invalid Input Type**: For non-integer or non-positive integer inputs where a positive integer is expected, display "Invalid input. Please enter a positive number."
-   **Invalid Choice**: For menu choices outside the valid range, display "Invalid choice. Please enter a number between 1 and 6."
-   **Empty Description**: For empty task descriptions, display "Task description cannot be empty."
-   **Task Not Found**: For operations on a non-existent task ID, display "Error: Task with ID [ID] not found."
-   All errors MUST be handled gracefully, preventing application crashes, and returning the user to the main menu or a clear prompt.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: Users can successfully add, view, update, complete, and delete todo items through the CLI without encountering unhandled errors.
-   **SC-002**: All user inputs are validated, and appropriate error messages are displayed for invalid or missing data.
-   **SC-003**: The application adheres to the defined folder structure (`/src/models.py`, `/src/services.py`, `/src/main.py`).
-   **SC-004**: Code coverage for core logic (TodoService) is at least 90%, demonstrating adherence to TDD.
-   **SC-005**: The application's core functionality (add, view, update, complete, delete) is demonstrable as a Minimum Viable Product (MVP).
