from .task import Task

class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, title, description):
        task = Task(title=title, description=description)
        self.tasks.append(task)
        self.storage.save(self.tasks)
        return task

    def list_tasks(self):
        return self.tasks

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            self.storage.save(self.tasks)
            return deleted
        else:
            raise IndexError("Task index out of range.")

    def update_task(self, index, title=None, description=None, done=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if done is not None:
                task.done = done
            self.storage.save(self.tasks)
            return task
        else:
            raise IndexError("Task index out of range.")
