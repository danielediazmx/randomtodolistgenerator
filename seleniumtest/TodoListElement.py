from typing import List


class TodoListElement:
    def __init__(self, name: str, description: str, categories: List[str], time_and_unit: str):
        self.name: str = name
        self.description: str = description
        self.categories: List[str] = categories
        self.time_and_unit: str = time_and_unit
