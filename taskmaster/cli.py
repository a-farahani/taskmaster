import argparse
from .core import TaskManager
from .storage import JsonStorage

def main():
    storage = JsonStorage("tasks.json")
    manager = TaskManager(storage)

    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("description", help="Task description")

    # List tasks
    subparsers.add_parser("list", help="List all tasks")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Index of task to delete")

    # Update task
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("index", type=int, help="Index of task to update")
    update_parser.add_argument("--title", help="New title")
    update_parser.add_argument("--description", help="New description")
    update_parser.add_argument("--done", choices=["True", "False"], help="Mark as done (True/False)")

    args = parser.parse_args()

    if args.command == "add":
        task = manager.add_task(args.title, args.description)
        print(f"Task added: {task.title}")

    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        for i, task in enumerate(tasks):
            status = "✓" if task.done else "✗"
            print(f"{i}: {task.title} - {task.description} [{status}]")

    elif args.command == "delete":
        try:
            deleted = manager.delete_task(args.index)
            print(f"Deleted task: {deleted.title}")
        except IndexError as e:
            print(f"Error: {e}")

    elif args.command == "update":
        try:
            done = None
            if args.done is not None:
                done = args.done.lower() == "true"
            print(done)
            updated = manager.update_task(
                args.index, args.title, args.description, done
            )
            print(f"Updated task: {updated.title}")
        except IndexError as e:
            print(f"Error: {e}")
