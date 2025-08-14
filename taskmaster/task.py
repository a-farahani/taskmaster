from dataclasses import dataclass, asdict

@dataclass
class Task:
    title: str
    description: str
    done: bool = False

    def to_dict(self):
        return asdict(self)
