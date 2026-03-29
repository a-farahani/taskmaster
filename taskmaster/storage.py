import json
from pathlib import Path
from .task import Task

class Storage:
    def load(self):
        raise NotImplementedError

    def save(self, tasks):
        raise NotImplementedError


class JsonStorage(Storage):
    def __init__(self, filepath):
        self.filepath = Path(filepath)

    def load(self):
        if not self.filepath.exists():
            return []
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Task(**item) for item in data]

    def save(self, tasks):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
