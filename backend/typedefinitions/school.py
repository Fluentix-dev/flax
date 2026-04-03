from .classroom import Class
from typing import List

class School:
    def __init__(self, name: str, classes: List[Class], id: str):
        self.name = name
        self.classes = classes
        self.id = id
    
    def __repr__(self):
        return f"<School><name>{self.name}</><classes>{self.classes}</><id>{self.id}</></>"