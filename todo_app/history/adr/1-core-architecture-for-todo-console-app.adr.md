# ADR-1: Core Architecture for Todo Console App

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-07
- **Feature:** todo-app-phase1
- **Context:** This ADR documents the fundamental architectural decisions for Phase I of the Todo Console Application, including data storage, application structure, task ID management, error handling, and CLI design. These choices underpin the development of a modular, clean, and user-centric Python console application.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

*   **In-Memory List for Todo Storage**: An in-memory Python dictionary (mapping IDs to `TodoItem` objects) is used for storing todo items for the duration of the application's runtime.
    *   **Rationale**: This aligns with the "Phase I" scope of building a simple console application without external dependencies or persistent storage requirements. It simplifies development and keeps the focus on core application logic and CLI interaction.
*   **Python Files Separated into `models.py`, `services.py`, `main.py`**: The application's codebase is strictly organized into these three modules within the `src/` directory.
    *   **Rationale**: This adheres to the "Modularity" and "Clean Code" principles outlined in the project constitution.
        *   `models.py`: Encapsulates data structures (`TodoItem` class), promoting a single responsibility for data representation.
        *   `services.py`: Contains all business logic (`TodoService` class) for managing todo items, separating concerns from data representation and user interface.
        *   `main.py`: Manages the CLI interface, menu display, user input, and orchestrates calls to the `TodoService`, ensuring a clear separation of presentation logic.
*   **Auto-Incrementing Task IDs**: New todo items are assigned unique, auto-incrementing integer IDs starting from 1.
    *   **Rationale**: Simplifies ID management for an in-memory application, ensures uniqueness, and provides a straightforward mechanism for users to reference tasks.
*   **Centralized Error Handling and Input Validation**: Error handling rules are defined in the `spec.md` and implemented across `TodoService` (for business logic validation) and `main.py` (for CLI input parsing and displaying user-friendly messages).
    *   **Rationale**: Adheres to the "Error Handling" principle, ensuring the application gracefully handles invalid inputs (non-integer IDs, empty descriptions, non-existent tasks) without crashing, and provides consistent, informative feedback to the user.
*   **CLI Menu-Driven Format**: The application uses a clear, numbered menu system in `main.py` for all user interactions.
    *   **Rationale**: Prioritizes "User-Centric Design" by providing an intuitive and easy-to-navigate interface, as specified in the `spec.md` and constitution.

## Consequences

### Positive

*   **Simplicity**: In-memory storage simplifies initial development and reduces complexity.
*   **Maintainability**: Clear separation of concerns (models, services, CLI) enhances code readability, testability, and maintainability.
*   **User Experience**: Consistent CLI and error messages improve usability.
*   **Foundation for Scalability**: The modular structure provides a solid foundation for future extensions, such as adding persistent storage or a different UI, without major refactoring of core logic.

### Negative

*   **No Persistence**: Todo items are lost when the application restarts, which is acceptable for Phase I but would require a new decision for persistence in future phases.
*   **Limited UI**: Restricted to a console interface, which limits advanced user interaction features.

## Alternatives Considered

*   **Data Storage**:
    *   **File-based storage (e.g., JSON, CSV)**: Rejected for Phase I to maintain simplicity and focus on core logic, but is a strong candidate for future persistence.
    *   **SQLite database**: Rejected due to adding external dependency and setup complexity for Phase I's minimal scope.
*   **Application Structure**:
    *   **Monolithic structure (all logic in `main.py`)**: Rejected as it violates "Modularity" and "Clean Code" principles, leading to unmanageable code.
*   **Task ID Generation**:
    *   **UUIDs**: Rejected for Phase I due to increased complexity and less human-readable IDs for a simple console application.

## References

- Feature Spec: specs/todo-app-phase1/spec.md
- Implementation Plan: C:\Users\12\.claude\plans\nifty-hatching-kurzweil.md
- Related ADRs: N/A
- Evaluator Evidence: N/A