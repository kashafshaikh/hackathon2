# Feature: Evolution of Todo — Phase I Tasks

**Date**: 2025-12-07
**Feature Branch**: `feature/todo-app-phase1`
**Source Plan**: C:\Users\12\.claude\plans\nifty-hatching-kurzweil.md
**Source Spec**: C:\Users\12\hackathon2\todo_app\specs\todo-app-phase1\spec.md

## Phase 1: Setup

*   `Task Goal`: Establish the foundational project structure and basic environment.
*   `Independent Test Criteria`: All required directories and empty placeholder files are created, and Python package structure is set up.

- [X] T001 Create `src` directory C:\Users\12\hackathon2\todo_app\src\
- [ ] T002 Create `__init__.py` in `src` C:\Users\12\hackathon2\todo_app\src\__init__.py
- [ ] T003 Create `models.py` in `src` C:\Users\12\hackathon2\todo_app\src\models.py
- [ ] T004 Create `services.py` in `src` C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T005 Create `main.py` in `src` C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T006 Create `tests` directory C:\Users\12\hackathon2\todo_app\tests\
- [ ] T007 Create `__init__.py` in `tests` C:\Users\12\hackathon2\todo_app\tests\__init__.py
- [ ] T008 Create `test_models.py` in `tests` C:\Users\12\hackathon2\todo_app\tests\test_models.py
- [ ] T009 Create `test_services.py` in `tests` C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T010 Create `test_main.py` in `tests` C:\Users\12\hackathon2\todo_app\tests\test_main.py

## Phase 2: Foundational Components (TodoItem Model)

*   `Task Goal`: Implement the core `TodoItem` data model and its unit tests.
*   `Independent Test Criteria`: The `TodoItem` class correctly initializes, updates its `completed` status, and provides a proper string representation. All `test_models.py` unit tests pass.

- [ ] T011 [P] Implement `TodoItem` class attributes (`id`, `description`, `completed`) in C:\Users\12\hackathon2\todo_app\src\models.py
- [ ] T012 [P] Implement `__init__` method for `TodoItem` in C:\Users\12\hackathon2\todo_app\src\models.py
- [ ] T013 [P] Implement `mark_complete` method for `TodoItem` in C:\Users\12\hackathon2\todo_app\src\models.py
- [ ] T014 [P] Implement `mark_incomplete` method for `TodoItem` in C:\Users\12\hackathon2\todo_app\src\models.py
- [ ] T015 [P] Implement `__repr__` method for `TodoItem` in C:\Users\12\hackathon2\todo_app\src\models.py
- [ ] T016 Write unit tests for `TodoItem` initialization in C:\Users\12\hackathon2\todo_app\tests\test_models.py
- [ ] T017 Write unit tests for `mark_complete` and `mark_incomplete` in C:\Users\12\hackathon2\todo_app\tests\test_models.py
- [ ] T018 Write unit tests for `__repr__` in C:\Users\12\hackathon2\todo_app\tests\test_models.py

## Phase 3: User Story 1 - Add Task (P1)

*   `Story Goal`: Users can add new todo items to their list by providing a description.
*   `Independent Test Criteria`: A user can launch the application, add a new todo item (e.g., "Buy groceries"), and then view the list to confirm the item is present. Attempting to add an empty description displays an error. All relevant unit and integration tests pass.

- [ ] T019 [US1] Implement `_next_id` and `_tasks` internal state for `TodoService` in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T020 [US1] Implement `add_task(self, description: str)` method in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T021 [US1] Implement description validation (non-empty) in `add_task` in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T022 [US1] Write unit tests for `TodoService.add_task` (including empty description error) in C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T023 [US1] Implement `get_user_input(prompt: str)` helper function in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T024 [US1] Implement main application loop and "Add Task" option in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T025 [US1] Add integration tests for "Add Task" CLI flow (including empty description) in C:\Users\12\hackathon2\todo_app\tests\test_main.py

## Phase 4: User Story 2 - View Tasks (P1)

*   `Story Goal`: Users can view a list of all existing todo items, including their unique ID, description, and status.
*   `Independent Test Criteria`: A user can add multiple todo items, and then select "View Tasks" to see all added tasks displayed correctly with their status. A message indicating no tasks is displayed when the list is empty. All relevant unit and integration tests pass.

- [ ] T026 [US2] Implement `list_tasks(self) -> List[TodoItem]` method in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T027 [US2] Write unit tests for `TodoService.list_tasks` (empty and non-empty list) in C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T028 [US2] Implement `display_menu()` function in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T029 [US2] Add "View Tasks" option to the CLI menu and implement its logic in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T030 [US2] Add integration tests for "View Tasks" CLI flow (empty and non-empty list) in C:\Users\12\hackathon2\todo_app\tests\test_main.py

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (P2)

*   `Story Goal`: Users can change the status of an existing todo item between "pending" and "completed" using its unique ID.
*   `Independent Test Criteria`: A user can add a task, view it, then mark it complete. Viewing the list again should show the task as "completed". Subsequently, they can mark it incomplete, and viewing the list should reflect the change. Handling of non-existent IDs and redundant status changes should display informative messages. All relevant unit and integration tests pass.

- [ ] T031 [US3] Implement `get_task(self, task_id: int) -> Optional[TodoItem]` method in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T032 [US3] Implement `mark_task_complete(self, task_id: int) -> Optional[TodoItem]` method in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T033 [US3] Implement `mark_task_incomplete(self, task_id: int) -> Optional[TodoItem]` method in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T034 [US3] Write unit tests for `TodoService.get_task` (existent and non-existent IDs) in C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T035 [US3] Write unit tests for `TodoService.mark_task_complete` (pending, completed, non-existent) in C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T036 [US3] Write unit tests for `TodoService.mark_task_incomplete` (completed, pending, non-existent) in C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T037 [US3] Add "Mark Complete/Incomplete" option to CLI menu and implement logic, including ID validation and error messages in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T038 [US3] Add integration tests for "Mark Complete/Incomplete" CLI flow (valid, non-existent, already in status) in C:\Users\12\hackathon2\todo_app\tests\test_main.py

## Phase 6: User Story 4 - Update Task (P2)

*   `Story Goal`: Users can modify the description of an existing todo item using its unique ID.
*   `Independent Test Criteria`: A user can add a task, view it, then update its description. Viewing the list again should show the updated description. Handling of non-existent IDs, non-positive integer IDs, and empty new descriptions should display informative messages. All relevant unit and integration tests pass.

- [ ] T039 [US4] Implement `update_task(self, task_id: int, new_description: str) -> Optional[TodoItem]` method in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T040 [US4] Implement description validation (non-empty) in `update_task` in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T041 [US4] Write unit tests for `TodoService.update_task` (valid update, empty description, non-existent ID) in C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T042 [US4] Add "Update Task" option to CLI menu and implement logic, including ID and description validation in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T043 [US4] Add integration tests for "Update Task" CLI flow (valid, non-existent ID, empty description) in C:\Users\12\hackathon2\todo_app\tests\test_main.py

## Phase 7: User Story 5 - Delete Task (P3)

*   `Story Goal`: Users can remove an existing todo item from the list using its unique ID.
*   `Independent Test Criteria`: A user can add a task, view it, then delete it. Viewing the list again should show the task is no longer present. Handling of non-existent IDs and non-positive integer IDs should display informative messages. All relevant unit and integration tests pass.

- [ ] T044 [US5] Implement `delete_task(self, task_id: int) -> bool` method in C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T045 [US5] Write unit tests for `TodoService.delete_task` (existent and non-existent IDs) in C:\Users\12\hackathon2\todo_app\tests\test_services.py
- [ ] T046 [US5] Add "Delete Task" option to CLI menu and implement logic, including ID validation in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T047 [US5] Add integration tests for "Delete Task" CLI flow (valid, non-existent ID) in C:\Users\12\hackathon2\todo_app\tests\test_main.py

## Phase 8: Polish & Cross-Cutting Concerns

*   `Task Goal`: Ensure robustness, graceful exit, and overall adherence to NFRs.
*   `Independent Test Criteria`: Application terminates gracefully on exit. All error handling rules are properly implemented and displayed to the user.

- [ ] T048 Implement graceful exit for the CLI application in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T049 Implement invalid menu choice error handling in C:\Users\12\hackathon2\todo_app\src\main.py
- [ ] T050 Ensure all error messages conform to `spec.md` (e.g., "Invalid input. Please enter a positive number.", "Task description cannot be empty.", "Error: Task with ID [ID] not found.") in C:\Users\12\hackathon2\todo_app\src\main.py and C:\Users\12\hackathon2\todo_app\src\services.py
- [ ] T051 Refine user prompts and display formatting for clarity and usability across `main.py` and `services.py`
- [ ] T052 Review and confirm adherence to PEP 8 guidelines across all Python files in `src/`

## Dependencies

The following outlines the recommended order of user story completion:

1.  Phase 1: Setup
2.  Phase 2: Foundational Components (TodoItem Model)
3.  Phase 3: User Story 1 - Add Task (P1)
4.  Phase 4: User Story 2 - View Tasks (P1)
5.  Phase 5: User Story 3 - Mark Task Complete/Incomplete (P2)
6.  Phase 6: User Story 4 - Update Task (P2)
7.  Phase 7: User Story 5 - Delete Task (P3)
8.  Phase 8: Polish & Cross-Cutting Concerns

Each user story phase is designed to be largely independent once its foundational components (models, basic service methods) are in place.

## Parallel Execution Examples

The tasks are designed for incremental, sequential implementation as per the TDD flow. However, within certain phases, if team members are working on distinct files with no direct dependencies on concurrently incomplete tasks, some parallelization is possible. For instance:

*   **During Phase 1 (Setup)**: Tasks T001-T010 (creating directories and empty files) can be done in parallel.
*   **During Phase 2 (TodoItem Model)**: Tasks T011-T015 (implementing `TodoItem` methods) can be parallelized, as can T016-T018 (writing unit tests for `TodoItem`) once the model methods are defined.
*   **Within User Story Phases**: Tasks involving independent file modifications (e.g., implementing a `TodoService` method and writing its unit test) can be worked on concurrently by different individuals, provided strict coordination and clear ownership.

## Implementation Strategy

The implementation will follow an MVP-first, incremental delivery approach, driven by Test-Driven Development (TDD). Each user story will be implemented as a complete, testable increment, starting with P1 features and progressing to P3. Automated tests will be written before or alongside implementation to ensure correctness and prevent regressions.

## Suggested MVP Scope

For an initial Minimum Viable Product (MVP), focus on implementing and thoroughly testing **User Story 1 (Add Task)** and **User Story 2 (View Tasks)**. These two stories provide the most essential core functionality for a todo application, allowing users to create and see their tasks.
