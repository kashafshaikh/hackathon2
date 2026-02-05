---

description: "Task list template for feature implementation"
---

# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!-- 
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.
  
  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/
  
  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  
  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure (`src/`, `tests/`) as per plan.
- [ ] T002 Initialize Python project with `pytest` for testing.
- [ ] T003 [P] Configure `flake8` and `black` for linting and formatting.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T004 Define `TodoItem` data structure in `src/models/todo.py` (Principle: Modularity).
- [ ] T005 Implement `TodoService` for managing todo items in `src/services/todo_service.py` (Principle: Modularity).
- [ ] T006 Configure basic error handling for invalid inputs in `src/cli/app.py` (Principle: Error Handling).
- [ ] T007 Setup command-line argument parsing for basic operations in `src/cli/app.py` (Principle: User-Centric Design).

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todo items to the list.

**Independent Test**: A user can add a todo item, and it appears in the list.

### Tests for User Story 1 (REQUIRED) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T008 [P] [US1] Unit test for adding a todo item in `tests/unit/test_todo_service.py`.
- [ ] T009 [P] [US1] Integration test for CLI `add` command in `tests/integration/test_cli.py`.

### Implementation for User Story 1

- [ ] T010 [US1] Add `add_todo` method to `TodoService` in `src/services/todo_service.py`.
- [ ] T011 [US1] Implement CLI command for `add` functionality in `src/cli/app.py`.
- [ ] T012 [US1] Add input validation for todo description (Principle: Error Handling).

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: Allow users to view all active todo items.

**Independent Test**: A user can view a list of todo items, including newly added ones.

### Tests for User Story 2 (REQUIRED) ⚠️

- [ ] T013 [P] [US2] Unit test for retrieving todo items in `tests/unit/test_todo_service.py`.
- [ ] T014 [P] [US2] Integration test for CLI `list` command in `tests/integration/test_cli.py`.

### Implementation for User Story 2

- [ ] T015 [US2] Add `get_todos` method to `TodoService` in `src/services/todo_service.py`.
- [ ] T016 [US2] Implement CLI command for `list` functionality in `src/cli/app.py`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P2)

**Goal**: Allow users to mark an existing todo item as complete.

**Independent Test**: A user can mark a todo item as complete, and its status updates in the list.

### Tests for User Story 3 (REQUIRED) ⚠️

- [ ] T017 [P] [US3] Unit test for marking todo item complete in `tests/unit/test_todo_service.py`.
- [ ] T018 [P] [US3] Integration test for CLI `complete` command in `tests/integration/test_cli.py`.

### Implementation for User Story 3

- [ ] T019 [US3] Add `complete_todo` method to `TodoService` in `src/services/todo_service.py`.
- [ ] T020 [US3] Implement CLI command for `complete` functionality in `src/cli/app.py`.
- [ ] T021 [US3] Add error handling for invalid todo IDs (Principle: Error Handling).

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: User Story 4 - Delete Todo (Priority: P2)

**Goal**: Allow users to remove a todo item from the list.

**Independent Test**: A user can delete a todo item, and it is no longer present in the list.

### Tests for User Story 4 (REQUIRED) ⚠️

- [ ] T022 [P] [US4] Unit test for deleting a todo item in `tests/unit/test_todo_service.py`.
- [ ] T023 [P] [US4] Integration test for CLI `delete` command in `tests/integration/test_cli.py`.

### Implementation for User Story 4

- [ ] T024 [US4] Add `delete_todo` method to `TodoService` in `src/services/todo_service.py`.
- [ ] T025 [US4] Implement CLI command for `delete` functionality in `src/cli/app.py`.
- [ ] T026 [US4] Add error handling for invalid todo IDs (Principle: Error Handling).

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security hardening
- [ ] TXXX Run quickstart.md validation

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

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
Task: "Contract test for [endpoint] in tests/contract/test_[name].py"
Task: "Integration test for [user journey] in tests/integration/test_[name].py"

# Launch all models for User Story 1 together:
Task: "Create [Entity1] model in src/models/[entity1].py"
Task: "Create [Entity2] model in src/models/[entity2].py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
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
