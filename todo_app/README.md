# Phase I – Colorful Todo Console Application

A Python-based in-memory todo console application with colorful CLI interface.

## Features

- **Add Task**: Add new tasks with title and description
- **View Tasks**: View all tasks with ID, title, description, and status
- **Update Task**: Update existing tasks by ID
- **Delete Task**: Remove tasks by ID
- **Toggle Completion**: Mark tasks as completed/incomplete
- **Colorful Interface**: Enhanced with colors using colorama library
- **Robust Error Handling**: Comprehensive validation and error messages

## Requirements

- Python 3.13+
- colorama library

## Installation

1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python src/main.py
```

The application will display a menu-driven interface with the following options:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Task Completion
6. Exit

## Color Scheme

- **Menu numbers (1-6)**: Cyan
- **Menu text**: White
- **"Pending" status**: Yellow
- **"Completed" status**: Green
- **Success messages**: Green
- **Error messages**: Red
- **Navigation prompts**: Cyan

## Architecture

The application follows a clean layered architecture:

- **src/models.py**: Data models and in-memory storage
- **src/services.py**: Business logic layer
- **src/main.py**: Menu-driven CLI interface with color enhancements

## Functionality

### Add Task
- Prompts for task title (required) and description (optional)
- Validates that title is not empty
- Automatically assigns an incremented ID
- Sets initial status to "Pending"

### View All Tasks
- Displays all tasks in a formatted table
- Shows ID, Title, Description, and Status columns
- Colors "Pending" status in yellow and "Completed" status in green

### Update Task
- Prompts for task ID to update
- Allows updating title and/or description
- Validates that at least one field is provided for update
- Shows appropriate success/error messages

### Delete Task
- Prompts for task ID to delete
- Removes task from memory
- Shows confirmation or error message

### Toggle Task Completion
- Prompts for task ID to toggle
- Switches task status between "Pending" and "Completed"
- Shows appropriate success/error messages

### Exit
- Gracefully exits the application

## Error Handling

- Invalid menu choices are handled gracefully
- Non-existent task IDs show appropriate error messages
- Empty title validation prevents invalid task creation
- Invalid numeric input is handled with re-prompting
- Special characters and Unicode are handled safely
- Ctrl+C and Ctrl+D are handled gracefully

## File Structure

```
src/
├── main.py        # Menu-driven interface with color enhancements
├── models.py      # Data models and in-memory storage
├── services.py    # Business logic layer
├── __init__.py    # Package initialization
requirements.txt   # Python dependencies
README.md         # This file
```

## Development

All code follows PEP 8 standards with proper type hints and documentation.

## License

This project is available as part of the hackathon submission.