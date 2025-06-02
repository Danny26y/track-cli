import sys
import os
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):  # Ensure data is a list
                print("Error: tasks.json contains invalid data. Starting with an empty task list.")
                return []
            return data
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    print("Tasks to save:", tasks)  # Debug line
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def get_next_id(tasks):
    return max([task['id']for task in tasks], default=0)+1

def add_task(description):
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "description":description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task{task_id}updated successfully")
            return
    print(f"Error: Task with ID {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")

def mark_task(task_id, status):
    if status not in["in-progress", "done"]:
        print("Error: invalid status. Use 'in-progress' or 'done'")
        return
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Error: Task with ID {task_id} not found")

def list_tasks(status=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    filtered_tasks = tasks if status is None else[task for task in tasks if task['status'] == status]
    if not filtered_tasks:
        print(f"No tasks with status '{status}' found")
        return
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}"f"Created: {task['createdAt']}, Updated; {task['updatedAt']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [args]")
        print("Commands: add, update, delete, mark-in-progress, mark-done list[done|todo|in-progress")
        return
    command = sys.argv[1].lower()
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Description is required for add command")
                return
            description = sys.argv[2]
            add_task(description)
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Task ID and description are required for update command")
                return
            task_id = int(sys.argv[2])
            description = sys.argv[3]
            update_task(task_id, description)
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Task ID is required for delete command")
                return
            task_id = int(sys.argv[2])
            delete_task(task_id)
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Task ID is required for mark-in-progress command")
                return
            task_id = int(sys.argv[2])
            mark_task(task_id, "in-progress")
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Task ID is required for mark_done command")
                return
            task_id = int(sys.argv[2])
            mark_task(task_id, "done")
        elif command == "list":
            status = sys.argv[2].lower() if len(sys.argv) > 2 else None
            if status not in [None, "done", "todo", "in-progress"]:
                print("Error: Invalid status. Use 'done' , 'todo', or 'in-progress'.")
                return
            list_tasks(status)
        else:
            print(f"Error: Unknown command '{command}'")
            print("Command: add, update, delete, mark-in-progress, mark-done, list [done|todo|in-progress")
    except ValueError:
        print("Error: Task ID must be a number")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

