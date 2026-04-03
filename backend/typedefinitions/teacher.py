"""
Describes a teacher
"""

from .person import Person, Gender
from .datastructures import Date
from backend.tools.contact import ContactInfo
from .subject import Subject
from typing import List

class Teacher(Person):
    """
    Base class for a teacher
    """
    def __init__(self, name: str, dob: Date, gender: Gender, teachingSubjects: List[Subject], contactInfos: List[ContactInfo], id: str):
        # no need parent info for teachers
        super().__init__(name, dob, gender, contactInfos, id)
        self.teachingSubjects = teachingSubjects

    
    def __repr__(self):
        return f"<Student><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}><contactInfos><{self.contactInfos}><id>{self.id}</><teachingSubjects>{self.teachingSubjects}</></>"