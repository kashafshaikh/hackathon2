"""
Main entry point for the Todo Console Application.
Implements a menu-driven interface for task management with color enhancement.
"""

import sys
import os
from colorama import init, Fore, Style
# Initialize colorama for cross-platform color support
init(autoreset=True)

# Add the src directory to the path so imports work
sys.path.insert(0, os.path.dirname(__file__))

from services import TaskService


def get_user_input(prompt: str) -> str:
    """
    Safely get user input with error handling.

    Args:
        prompt: Prompt to display to the user

    Returns:
        User input string
    """
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Exiting application...")
        exit(0)
    except EOFError:
        print(f"\n\n{Fore.YELLOW}Exiting application...")
        exit(0)


def get_integer_input(prompt: str) -> int:
    """
    Get integer input from user with validation.

    Args:
        prompt: Prompt to display to the user

    Returns:
        Integer value entered by user
    """
    while True:
        user_input = get_user_input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print(f"{Fore.RED}Error: Please enter a valid number.")


def display_menu():
    """Display the main menu options with colors."""
    print(f"\n{Fore.CYAN}Todo Console Application")
    print(f"{Fore.CYAN}=======================")
    print(f"{Fore.CYAN}1{Fore.WHITE}. Add Task")
    print(f"{Fore.CYAN}2{Fore.WHITE}. View All Tasks")
    print(f"{Fore.CYAN}3{Fore.WHITE}. Update Task")
    print(f"{Fore.CYAN}4{Fore.WHITE}. Delete Task")
    print(f"{Fore.CYAN}5{Fore.WHITE}. Toggle Task Completion")
    print(f"{Fore.CYAN}6{Fore.WHITE}. Exit")
    print()


def colorize_task_list(task_list_str: str) -> str:
    """
    Add colors to the task list output.

    Args:
        task_list_str: The original task list string

    Returns:
        The task list string with color codes applied to status
    """
    lines = task_list_str.split('\n')
    colored_lines = []

    for line in lines:
        if 'Pending' in line:
            # Color the 'Pending' text red
            colored_line = line.replace('Pending', f'{Fore.YELLOW}Pending{Style.RESET_ALL}')
        elif 'Completed' in line:
            # Color the 'Completed' text green
            colored_line = line.replace('Completed', f'{Fore.GREEN}Completed{Style.RESET_ALL}')
        else:
            colored_line = line
        colored_lines.append(colored_line)

    return '\n'.join(colored_lines)


def colorize_message(message: str) -> str:
    """
    Colorize success and error messages.

    Args:
        message: The original message string

    Returns:
        The message with appropriate color codes
    """
    if message.startswith("Error:") or "Error:" in message:
        return f"{Fore.RED}{message}{Style.RESET_ALL}"
    elif "successfully" in message or message.startswith("Task #"):
        return f"{Fore.GREEN}{message}{Style.RESET_ALL}"
    else:
        return message


def main():
    """Main application loop."""
    service = TaskService()

    while True:
        display_menu()

        choice = get_user_input("Enter your choice (1-6): ")

        if choice == "1":
            # Add Task
            title = get_user_input("Enter task title: ")
            if not title:
                print(f"{Fore.RED}Error: Title cannot be empty.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                continue

            description = get_user_input("Enter task description (optional, press Enter to skip): ")

            result = service.add_task(title, description)
            print(colorize_message(result))

        elif choice == "2":
            # View All Tasks
            result = service.view_all_tasks()
            colored_result = colorize_task_list(result)
            print(colored_result)

        elif choice == "3":
            # Update Task
            if not service.storage.get_all_tasks():
                print(f"{Fore.YELLOW}No tasks available to update.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                continue

            task_id = get_integer_input("Enter task ID to update: ")

            # Check if the task exists
            task = service.get_task_by_id(task_id)
            if not task:
                print(f"{Fore.RED}Error: Task with ID {task_id} not found")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                continue

            print("Leave fields empty to keep current values.")
            new_title = get_user_input("Enter new title (or press Enter to keep current): ")
            new_desc = get_user_input("Enter new description (or press Enter to keep current): ")

            # If both are empty, don't update
            if not new_title and not new_desc:
                print("No changes provided, task not updated.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                continue

            # Prepare parameters for update
            title_param = new_title if new_title else None
            desc_param = new_desc if new_desc else None

            result = service.update_task(task_id, title_param, desc_param)
            print(colorize_message(result))

        elif choice == "4":
            # Delete Task
            if not service.storage.get_all_tasks():
                print(f"{Fore.YELLOW}No tasks available to delete.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                continue

            task_id = get_integer_input("Enter task ID to delete: ")

            result = service.delete_task(task_id)
            print(colorize_message(result))

        elif choice == "5":
            # Toggle Task Completion
            if not service.storage.get_all_tasks():
                print(f"{Fore.YELLOW}No tasks available to toggle.")
                input(f"\n{Fore.CYAN}Press Enter to continue...")
                continue

            task_id = get_integer_input("Enter task ID to toggle completion: ")

            result = service.toggle_task_completion(task_id)
            print(colorize_message(result))

        elif choice == "6":
            # Exit
            print(f"{Fore.GREEN}Thank you for using the Todo Console Application!")
            break

        else:
            print(f"{Fore.RED}Error: Invalid choice. Please enter a number between 1-6.")

        # Pause to let user see the result before showing menu again
        input(f"\n{Fore.CYAN}Press Enter to continue...")


if __name__ == "__main__":
    main()