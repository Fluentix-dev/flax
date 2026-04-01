"""
Describes a class (or a classroom).
"""

from enum import Enum, auto
from typing import List
from student import Student
from teacher import Teacher

class ClassroomType(Enum):
    """
    Shows the type of a classroom. A normal 'classroom' is a place where
    students learn. A homeroom is a class where some students based on.
    A classroom can be both a classroom and homeroom.
    """
    Classroom = auto(),
    Homeroom = auto(),
    Both = auto()

    def __str__(self):
        return f"<ClassroomType>{self.name}</>"


class Class:
    """
    A class that describes a school class; containing all the students, teachers.
    """
    def __init__(self, students: List[Student], teachers: List[Teacher], id: str, classroomType: ClassroomType):
        self.students = students
        self.teachers = teachers
        self.id = id
        self.classroomType = classroomType
    

    def __str__(self):
        return f"<Class><students>{self.students}</><teachers>{self.teachers}</><id>{self.id}</><classroomType>{self.classroomType}</></>"