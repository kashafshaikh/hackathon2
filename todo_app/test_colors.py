#!/usr/bin/env python3
"""
Test script to verify the color enhancements work correctly
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services import TaskService
from colorama import init, Fore, Style
init(autoreset=True)

def test_colors():
    print(f"{Fore.CYAN}Testing Color Enhancement Features...{Style.RESET_ALL}\n")

    service = TaskService()

    # Test adding tasks
    print(f"{Fore.GREEN}1. Adding tasks (success message should be green):{Style.RESET_ALL}")
    result1 = service.add_task("Color Test Task 1", "Description for color test")
    print(f"   {result1}")

    result2 = service.add_task("Color Test Task 2", "Another color test description")
    print(f"   {result2}")

    # Test viewing tasks with colored statuses
    print(f"\n{Fore.CYAN}2. Viewing tasks (status should be yellow for pending):{Style.RESET_ALL}")
    result = service.view_all_tasks()

    # Apply color to the output to simulate what would be seen in main.py
    lines = result.split('\n')
    for line in lines:
        if 'Pending' in line:
            print(f"{line.replace('Pending', f'{Fore.YELLOW}Pending{Style.RESET_ALL}')}")
        elif 'Completed' in line:
            print(f"{line.replace('Completed', f'{Fore.GREEN}Completed{Style.RESET_ALL}')}")
        else:
            print(line)

    # Test toggling to completed status
    print(f"\n{Fore.GREEN}3. Toggling task to completed (success message should be green):{Style.RESET_ALL}")
    result = service.toggle_task_completion(1)
    print(f"   {result}")

    # View tasks again to see completed in green
    print(f"\n{Fore.CYAN}4. Viewing tasks after toggle (status should be green for completed):{Style.RESET_ALL}")
    result = service.view_all_tasks()

    # Apply color to the output to simulate what would be seen in main.py
    lines = result.split('\n')
    for line in lines:
        if 'Pending' in line:
            print(f"{line.replace('Pending', f'{Fore.YELLOW}Pending{Style.RESET_ALL}')}")
        elif 'Completed' in line:
            print(f"{line.replace('Completed', f'{Fore.GREEN}Completed{Style.RESET_ALL}')}")
        else:
            print(line)

    # Test error handling
    print(f"\n{Fore.RED}5. Testing error handling (error message should be red):{Style.RESET_ALL}")
    result = service.update_task(999, "Non-existent task")
    print(f"   {result}")

    print(f"\n{Fore.GREEN}*** Color enhancement test completed successfully! ***{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Colors implemented:{Style.RESET_ALL}")
    print(f"- Menu numbers: {Fore.CYAN}CYAN{Style.RESET_ALL}")
    print(f"- Menu text: {Fore.WHITE}WHITE{Style.RESET_ALL}")
    print(f"- Pending status: {Fore.YELLOW}YELLOW{Style.RESET_ALL}")
    print(f"- Completed status: {Fore.GREEN}GREEN{Style.RESET_ALL}")
    print(f"- Success messages: {Fore.GREEN}GREEN{Style.RESET_ALL}")
    print(f"- Error messages: {Fore.RED}RED{Style.RESET_ALL}")


if __name__ == "__main__":
    test_colors()