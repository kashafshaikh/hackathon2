# ADR 002: Architectural Decisions for Todo Console Application

## Status
Accepted

## Context
We needed to build a Phase I Todo Console Application that meets the following requirements:
- Menu-driven interface for task management
- In-memory storage only (no persistent storage)
- Clear separation of concerns
- Robust error handling
- User-friendly CLI experience

Various architectural approaches were considered for data storage, technology stack, application structure, and user interface design.

## Decision

### 1. In-Memory Storage with Python Dictionaries

**Decision**: Use Python dictionaries for in-memory storage instead of a database.

**Rationale**:
- The specification explicitly requires in-memory storage only, with no persistent storage
- Python dictionaries provide O(1) average-case complexity for lookup, insertion, and deletion
- Eliminates external dependencies on database systems
- Simpler to implement and maintain for a console application
- Suitable for the intended use case (short-lived sessions, small datasets)
- Faster performance compared to file I/O operations

**Alternative Considered**: SQLite database
- Rejected because it would introduce persistence, violating the in-memory requirement
- Would add unnecessary complexity for a simple application

### 2. Python Programming Language Selection

**Decision**: Choose Python 3.13+ as the implementation language.

**Rationale**:
- Rich standard library with built-in data structures (dicts, lists) perfect for in-memory storage
- Excellent string manipulation and formatting capabilities for CLI interface
- Strong typing support with type hints for code quality
- Cross-platform compatibility ensures broad usability
- Clear, readable syntax aligns with the "clean and readable" requirement
- Built-in exception handling for robust error management
- Extensive ecosystem and community support

**Alternative Considered**: Java or C#
- Rejected as they would introduce unnecessary complexity for a simple console application
- JVM/.NET runtime requirements would add overhead

### 3. Layered Architecture with Separation of Concerns

**Decision**: Separate the application into three distinct files: models.py, services.py, and main.py.

**Rationale**:
- **models.py**: Contains data structures and storage logic, enabling easy testing and maintenance of data operations
- **services.py**: Houses business logic and orchestrates operations, promoting reusability and clear API boundaries
- **main.py**: Manages user interface and application flow, keeping presentation concerns isolated
- Follows Single Responsibility Principle (SRP) - each module has one reason to change
- Enables easier unit testing by isolating concerns
- Improves code organization and maintainability
- Aligns with common architectural patterns (MVC-like separation)

**Alternative Considered**: Single file implementation
- Rejected because it would create a monolithic structure difficult to test and maintain
- Would violate the separation of concerns principle

### 4. Auto-Increment ID System

**Decision**: Implement auto-incrementing integer IDs starting from 1.

**Rationale**:
- Provides a simple, predictable identifier system that users can easily reference
- Ensures uniqueness without complex algorithms or external dependencies
- Integer comparison and lookup are efficient
- Natural progression makes IDs intuitive for users
- Prevents ID collisions and simplifies storage management
- Matches user expectation of sequential numbering
- Consistent with common application patterns

**Alternative Considered**: UUID/GUID system
- Rejected as it would create unnecessarily long and complex identifiers
- Less user-friendly for CLI interactions
- More complex implementation for a simple console application

### 5. Menu-Driven CLI Interface

**Decision**: Implement a menu-driven command-line interface instead of command-line arguments or GUI.

**Rationale**:
- Matches the specification requirement for a "menu-driven interface"
- Provides guided user experience suitable for console applications
- Reduces complexity of command parsing and validation
- Enables interactive session with immediate feedback
- Familiar pattern for users accustomed to terminal applications
- Allows for richer interaction patterns than simple command arguments
- Simpler to implement than GUI while maintaining usability
- Suitable for the target audience of console application users

**Alternative Considered**: Command-line arguments interface (e.g., `app.py add "task"`)
- Rejected because it would require users to remember complex commands
- Would provide less guidance for first-time users
- Would not match the specification requirement for a menu-driven interface

## Consequences

### Positive
- The application is lightweight with no external dependencies beyond Python standard library
- Performance is optimal for the intended use case
- Code is well-organized and maintainable
- User experience is intuitive and guided
- Testing is simplified by clear separation of concerns
- Implementation aligns perfectly with the specification requirements

### Negative
- Data is lost when application exits (by design)
- May not scale well for very large datasets (though this is outside the intended scope)
- Menu interface requires more interaction steps than direct command-line arguments

## References
- Original specification in `specs/todo-app/spec.md`
- Implementation in `src/models.py`, `src/services.py`, `src/main.py`
- Design considerations in `specs/todo-app/plan.md`

## Date
2026-02-05

## Authors
Claude Code