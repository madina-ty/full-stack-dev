import argparse
import json
import os

def load_tasks():
    """Load tasks from the tasks.json file."""
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the tasks.json file."""
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task with the given description."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'description': description})
    save_tasks(tasks)
    print(f'Task added: {task_id} - {description}')

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
        return
    for task in tasks:
        print(f"{task['id']}: {task['description']}")

def update_task(task_id, new_description):
    """Update the description of an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            save_tasks(tasks)
            print(f'Task {task_id} updated.')
            return
    print(f'Task {task_id} not found.')

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage your to-do list.')
    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('description', type=str, help='New description of the task')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        parser.print_help()


