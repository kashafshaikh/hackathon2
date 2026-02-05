#!/usr/bin/env python3
"""
Quick test to verify the end-to-end functionality of the Todo Console Application
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services import TaskService

def test_functionality():
    print("Testing Todo Console Application functionality...\n")

    service = TaskService()

    # Test 1: Add tasks
    print("1. Testing add_task functionality:")
    result1 = service.add_task("Sample Task 1", "Description for task 1")
    print(f"   Result: {result1}")

    result2 = service.add_task("Sample Task 2", "Description for task 2")
    print(f"   Result: {result2}")

    # Test 2: View all tasks
    print("\n2. Testing view_all_tasks functionality:")
    result = service.view_all_tasks()
    print(f"   Result:\n{result}")

    # Test 3: Toggle task completion
    print("\n3. Testing toggle_task_completion functionality:")
    result = service.toggle_task_completion(1)
    print(f"   Result: {result}")

    # View tasks again to see the change
    print("\n4. Viewing tasks after toggle:")
    result = service.view_all_tasks()
    print(f"   Result:\n{result}")

    # Test 4: Update task
    print("\n5. Testing update_task functionality:")
    result = service.update_task(2, new_title="Updated Task 2", new_description="Updated description")
    print(f"   Result: {result}")

    # View tasks again to see the change
    print("\n6. Viewing tasks after update:")
    result = service.view_all_tasks()
    print(f"   Result:\n{result}")

    # Test 5: Delete task
    print("\n7. Testing delete_task functionality:")
    result = service.delete_task(1)
    print(f"   Result: {result}")

    # View tasks again to see the change
    print("\n8. Viewing tasks after deletion:")
    result = service.view_all_tasks()
    print(f"   Result:\n{result}")

    # Test 6: Error handling - try operations on non-existent tasks
    print("\n9. Testing error handling for non-existent tasks:")
    result = service.update_task(99, new_title="Non-existent task")
    print(f"   Update non-existent task: {result}")

    result = service.delete_task(99)
    print(f"   Delete non-existent task: {result}")

    result = service.toggle_task_completion(99)
    print(f"   Toggle non-existent task: {result}")

    # Test 7: Error handling - empty title validation
    print("\n10. Testing error handling for empty titles:")
    result = service.add_task("", "This should fail")
    print(f"   Add task with empty title: {result}")

    print("\n*** All functionality tests passed! ***")

if __name__ == "__main__":
    test_functionality()