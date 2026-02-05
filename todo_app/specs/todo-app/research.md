# Research for Todo In-Memory Python Console App

## Decision: Console Argument Parsing
**Rationale**: Using Python's built-in `argparse` module provides robust command-line argument parsing with built-in help generation and error handling.
**Alternatives considered**:
- `sys.argv` - Basic but lacks advanced features
- Third-party libraries like `click` - Would violate "standard library only" constraint

## Decision: Data Storage Structure
**Rationale**: Using a dictionary with integer keys for todo IDs provides O(1) lookup performance and aligns with the in-memory requirement.
**Alternatives considered**:
- List-based storage - Would require linear search for updates/deletes
- Custom class wrapper - Unnecessary complexity for in-memory storage

## Decision: Task Priority Implementation
**Rationale**: Using an enum for priority levels ensures type safety and prevents invalid priority values.
**Alternatives considered**:
- String constants - Prone to typos and invalid values
- Integer values - Less readable and error-prone

## Decision: Date/Time Handling
**Rationale**: Using `datetime` from standard library for timestamps provides ISO formatting and timezone awareness.
**Alternatives considered**:
- Unix timestamps as integers - Less readable for debugging
- Custom string formats - Not standardized

## Decision: Error Handling Approach
**Rationale**: Custom exception classes provide specific error types that can be caught individually and provide meaningful messages.
**Alternatives considered**:
- Generic exceptions - Less specific error handling
- Return codes - Doesn't follow Python conventions

## Decision: CLI Output Formatting
**Rationale**: Using tabulate or formatted string literals provides clean, readable output tables for listing todos.
**Alternatives considered**:
- CSV format - Less human-readable
- Raw JSON - Not user-friendly for console app