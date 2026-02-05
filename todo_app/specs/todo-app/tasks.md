# Tasks: Todo Console Application Implementation

**Input**: Design documents from `/specs/todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure (`src/`) as per plan.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T002 Define `Task` data structure in `src/models.py` (Principle: Modularity).
- [ ] T003 Implement `InMemoryStorage` class for task storage in `src/models.py` (Principle: Modularity).
- [ ] T004 Configure basic error handling and validation in `src/models.py` (Principle: Error Handling).

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks with title and description.

**Independent Test**: A user can add a task with a title and description, and it appears in the system with a unique ID.

### Tests for User Story 1 (REQUIRED) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T005 [P] [US1] Unit test for adding a task with title and description in `tests/test_models.py`.
- [ ] T006 [P] [US1] Unit test for auto-increment ID functionality in `tests/test_models.py`.

### Implementation for User Story 1

- [ ] T007 [US1] Implement `add_task` method in `InMemoryStorage` class in `src/models.py`.
- [ ] T008 [US1] Add validation to prevent empty titles in `src/models.py`.
- [ ] T009 [US1] Implement `Task` constructor with validation in `src/models.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - View Tasks (Priority: P1)

**Goal**: Allow users to view all tasks with ID and status.

**Independent Test**: A user can view a list of tasks showing ID, title, description, and completion status.

### Tests for User Story 2 (REQUIRED) ⚠️

- [ ] T010 [P] [US2] Unit test for retrieving all tasks in `tests/test_models.py`.
- [ ] T011 [P] [US2] Unit test for formatted task display in `tests/test_services.py`.

### Implementation for User Story 2

- [ ] T012 [US2] Implement `get_all_tasks` method in `InMemoryStorage` in `src/models.py`.
- [ ] T013 [US2] Implement `view_all_tasks` method in `TaskService` in `src/services.py`.
- [ ] T014 [US2] Add formatted table display for tasks in `src/services.py`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Update Task (Priority: P1)

**Goal**: Allow users to modify an existing task by ID.

**Independent Test**: A user can update a task's title or description by ID.

### Tests for User Story 3 (REQUIRED) ⚠️

- [ ] T015 [P] [US3] Unit test for updating task title in `tests/test_models.py`.
- [ ] T016 [P] [US3] Unit test for updating task description in `tests/test_models.py`.

### Implementation for User Story 3

- [ ] T017 [US3] Implement `update_task` method in `InMemoryStorage` in `src/models.py`.
- [ ] T018 [US3] Implement `update_task` method in `TaskService` in `src/services.py`.
- [ ] T019 [US3] Add input validation for updates in `src/models.py`.

**Checkpoint**: At this point, User Stories 1, 2, and 3 should all work independently.

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Allow users to remove a task from the list by ID.

**Independent Test**: A user can delete a task by ID, and it's no longer accessible.

### Tests for User Story 4 (REQUIRED) ⚠️

- [ ] T020 [P] [US4] Unit test for deleting a task by ID in `tests/test_models.py`.
- [ ] T021 [P] [US4] Unit test for handling non-existent task deletion in `tests/test_models.py`.

### Implementation for User Story 4

- [ ] T022 [US4] Implement `delete_task` method in `InMemoryStorage` in `src/models.py`.
- [ ] T023 [US4] Implement `delete_task` method in `TaskService` in `src/services.py`.

---

## Phase 7: User Story 5 - Toggle Task Completion (Priority: P2)

**Goal**: Allow users to change a task's completion status (complete/incomplete).

**Independent Test**: A user can toggle a task's completion status by ID.

### Tests for User Story 5 (REQUIRED) ⚠️

- [ ] T024 [P] [US5] Unit test for toggling task completion status in `tests/test_models.py`.
- [ ] T025 [P] [US5] Unit test for verifying status alternation in `tests/test_models.py`.

### Implementation for User Story 5

- [ ] T026 [US5] Implement `toggle_task_completion` method in `InMemoryStorage` in `src/models.py`.
- [ ] T027 [US5] Implement `toggle_task_completion` method in `TaskService` in `src/services.py`.

---

## Phase 8: User Story 6 - Service Layer (Priority: P2)

**Goal**: Create business logic layer to manage task operations.

**Independent Test**: Business logic methods provide appropriate success/error messages.

### Tests for User Story 6 (REQUIRED) ⚠️

- [ ] T028 [P] [US6] Unit test for TaskService functionality in `tests/test_services.py`.

### Implementation for User Story 6

- [ ] T029 [US6] Create `TaskService` class in `src/services.py`.
- [ ] T030 [US6] Implement error handling in `TaskService` methods in `src/services.py`.
- [ ] T031 [US6] Add success/error message formatting in `src/services.py`.

---

## Phase 9: User Story 7 - CLI Menu System (Priority: P1)

**Goal**: Implement menu-driven command-line interface.

**Independent Test**: User can interact with the application through menu choices.

### Tests for User Story 7 (REQUIRED) ⚠️

- [ ] T032 [P] [US7] Unit test for menu display in `tests/test_main.py`.
- [ ] T033 [P] [US7] Unit test for menu choice processing in `tests/test_main.py`.

### Implementation for User Story 7

- [ ] T034 [US7] Create main application loop in `src/main.py`.
- [ ] T035 [US7] Implement menu display function in `src/main.py`.
- [ ] T036 [US7] Add choice processing logic for menu options in `src/main.py`.

---

## Phase 10: User Story 8 - Input Processing (Priority: P1)

**Goal**: Handle user input with validation and error handling.

**Independent Test**: Invalid inputs are handled gracefully with appropriate error messages.

### Tests for User Story 8 (REQUIRED) ⚠️

- [ ] T037 [P] [US8] Unit test for input validation in `tests/test_main.py`.
- [ ] T038 [P] [US8] Unit test for error handling in `tests/test_main.py`.

### Implementation for User Story 8

- [ ] T039 [US8] Implement `get_user_input` function with error handling in `src/main.py`.
- [ ] T040 [US8] Implement `get_integer_input` function with validation in `src/main.py`.
- [ ] T041 [US8] Add graceful exit handling (Ctrl+C, Ctrl+D) in `src/main.py`.

---

## Phase 11: User Story 9 - Menu Operations (Priority: P1)

**Goal**: Connect menu choices to task operations.

**Independent Test**: Each menu choice triggers the correct operation with proper result display.

### Tests for User Story 9 (REQUIRED) ⚠️

- [ ] T042 [P] [US9] Unit test for add task operation in `tests/test_main.py`.
- [ ] T043 [P] [US9] Unit test for view tasks operation in `tests/test_main.py`.
- [ ] T044 [P] [US9] Unit test for update task operation in `tests/test_main.py`.
- [ ] T045 [P] [US9] Unit test for delete task operation in `tests/test_main.py`.
- [ ] T046 [P] [US9] Unit test for toggle task operation in `tests/test_main.py`.

### Implementation for User Story 9

- [ ] T047 [US9] Connect menu choice 1 (Add Task) to service in `src/main.py`.
- [ ] T048 [US9] Connect menu choice 2 (View Tasks) to service in `src/main.py`.
- [ ] T049 [US9] Connect menu choice 3 (Update Task) to service in `src/main.py`.
- [ ] T050 [US9] Connect menu choice 4 (Delete Task) to service in `src/main.py`.
- [ ] T051 [US9] Connect menu choice 5 (Toggle Task) to service in `src/main.py`.
- [ ] T052 [US9] Connect menu choice 6 (Exit) to application termination in `src/main.py`.

---

## Phase 12: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T053 [P] Add consistent error messages throughout the application (Principle: Error Handling).
- [ ] T054 [P] Add input validation across all service methods (Principle: Error Handling).
- [ ] T055 Add type hints to all functions and methods (Principle: Clean Code).
- [ ] T056 Add docstrings to all classes and methods (Principle: Clean Code).
- [ ] T057 Code cleanup and refactoring following PEP 8 (Principle: Clean Code).
- [ ] T058 Test the complete application flow manually.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 6 (P2)**: Can start after Foundational (Phase 2) - Required by US7/US9
- **User Story 7 (P1)**: Can start after US6 is complete
- **User Story 8 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 9 (P1)**: Depends on US6, US7, US8 being complete

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for adding a task with title and description in tests/test_models.py"
Task: "Unit test for auto-increment ID functionality in tests/test_models.py"

# Launch all models for User Story 1 together:
Task: "Implement add_task method in InMemoryStorage class in src/models.py"
Task: "Add validation to prevent empty titles in src/models.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1, 6, 7, 8, 9)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 6: User Story 6 (Service Layer)
5. Complete Phase 7: User Story 7 (CLI Menu System)
6. Complete Phase 8: User Story 8 (Input Processing)
7. Complete Phase 9: User Story 9 (Menu Operations) - specifically add task operation
8. **STOP and VALIDATE**: Test adding tasks through the menu interface
9. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational + US1,6,7,8,9 → MVP with Add Task!
2. Add US2 (View Tasks) → Test independently → Deploy/Demo
3. Add US3 (Update Task) → Test independently → Deploy/Demo
4. Add US4 (Delete Task) → Test independently → Deploy/Demo
5. Add US5 (Toggle Task) → Test independently → Deploy/Demo
6. Add Polish → Final product → Release
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Stories 1, 2, 3 (models layer)
   - Developer B: User Stories 6, 7 (services and CLI layer)
   - Developer C: User Stories 8, 9 (input processing and integration)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence