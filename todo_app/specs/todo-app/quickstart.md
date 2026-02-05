# Quickstart Guide: Todo In-Memory Python Console App

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Run the application directly with Python

```bash
python src/main.py --help
```

## Basic Usage

### Add a Todo
```bash
python src/main.py add "Complete project documentation"
```

### List Todos
```bash
python src/main.py list
# Shows all todos

python src/main.py list completed
# Shows only completed todos

python src/main.py list pending
# Shows only pending todos
```

### Complete a Todo
```bash
python src/main.py complete 1
# Marks todo with ID 1 as completed
```

### Update a Todo
```bash
python src/main.py update 1 "Updated description"
# Updates the description of todo with ID 1
```

### Delete a Todo
```bash
python src/main.py delete 1
# Deletes todo with ID 1
```

### Search Todos
```bash
python src/main.py search "documentation"
# Finds todos containing "documentation" in the description
```

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions

### Project Structure
- `src/models/` - Data models and entity definitions
- `src/services/` - Business logic and operations
- `src/cli/` - Command-line interface components
- `tests/unit/` - Unit tests for individual components
- `tests/integration/` - Integration tests for CLI and services