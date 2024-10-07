# task.py
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed
    def mark_completed(self):
        self.completed = True
    def __repr__(self):
        return f"Task(title='{self.title}', description='{self.description}', category='{self.category}', completed={self.completed})"