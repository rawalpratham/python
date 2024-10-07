# todo.py
from task import Task
from file_handler import save_tasks, load_tasks

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks):
        status = "✓" if task.completed else "✗"
        print(f"{index + 1}. [{status}] {task.title} - {task.category}: {task.description}")

def add_task(tasks):
    """Add a new task."""
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    category = input("Enter the task category: ")
    new_task = Task(title, description, category)
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

def edit_task(tasks):
    """Edit an existing task."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            category = input("Enter new category (leave blank to keep current): ")
            if title:
                tasks[index].title = title
            if description:
                tasks[index].description = description
            if category:
                tasks[index].category = category
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Delete an existing task."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted Task: {removed_task.title}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].mark_completed()
            save_tasks(tasks)
            print(f"Marked '{tasks[index].title}' as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()
    while True:
        print("\nPersonal To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()