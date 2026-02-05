#!/usr/bin/env python3
"""
Demo script for the Todo Console Application
"""

from src.cli.todo_cli import TodoCLI

def demo():
    """Demonstrate the functionality of the todo app."""
    print("=== Todo Console App Demo ===\n")

    cli = TodoCLI()

    # Add some todos
    print("1. Adding todos...")
    cli.run(['add', 'Learn Python', '--priority', 'high'])
    cli.run(['add', 'Build a project', '--priority', 'medium'])
    cli.run(['add', 'Write documentation', '--priority', 'low'])
    print()

    # List all todos
    print("2. Listing all todos:")
    cli.run(['list'])
    print()

    # Complete a todo
    print("3. Completing todo #1...")
    cli.run(['complete', '1'])
    print()

    # List pending todos
    print("4. Listing pending todos:")
    cli.run(['list', 'pending'])
    print()

    # List completed todos
    print("5. Listing completed todos:")
    cli.run(['list', 'completed'])
    print()

    # Update a todo
    print("6. Updating todo #2...")
    cli.run(['update', '2', 'Build a great project', '--priority', 'high'])
    print()

    # Search todos
    print("7. Searching for 'project'...")
    cli.run(['search', 'project'])
    print()

    # Final list
    print("8. Final list of all todos:")
    cli.run(['list'])
    print()

    print("=== Demo completed successfully! ===")

if __name__ == "__main__":
    demo()