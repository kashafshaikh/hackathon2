# ADR 001: Data Model and Architecture Decision

## Status
Accepted

## Context
We needed to design a simple yet effective data model for a console-based todo application that operates entirely in memory. The application needed to support all core todo operations while maintaining clean separation of concerns.

## Decision
We chose to implement the following architecture:

1. **Data Model Layer** (`src/models/`):
   - `TodoItem` class to represent individual todo items
   - `TodoCollection` class for in-memory storage
   - Priority enum for consistent priority levels

2. **Service Layer** (`src/services/`):
   - `TodoService` class for business logic operations
   - Clean interface separating operations from implementation

3. **Presentation Layer** (`src/cli/`):
   - `TodoCLI` class for command-line interface
   - Argument parsing and user interaction

## Alternatives Considered

1. **Monolithic approach**: Put all functionality in a single file - rejected as it violates modularity principle
2. **Database storage**: Use SQLite or file storage - rejected as it violates the in-memory requirement
3. **Different CLI library**: Use Click instead of argparse - rejected as it would introduce external dependencies against the spec requirement

## Consequences

### Positive
- Clear separation of concerns following MVC pattern
- Easy to test individual components
-符合 modular design principles from the constitution
- Easy to extend with additional features

### Negative
- More complex than a single-file solution
- Requires careful import management between modules

## Rationale
This approach aligns with the architectural principles specified in the constitution:
- Modularity: Components are self-contained with single responsibility
- Clean Code: Following PEP 8 guidelines with clear naming
- Testability: Each component can be unit tested independently
- Maintainability: Clear interfaces between layers

## Date
2026-02-05

## Authors
Claude Code