# file_handler.py
import json
from task import Task

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []