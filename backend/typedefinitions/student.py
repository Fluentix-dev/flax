"""
Base script that defines a student.
"""

from __future__ import annotations
from functools import lru_cache
from typing import List, Optional, Set, Any
from collections.abc import Iterable
from .person import Person, Gender
from .datastructures import Date
from .subject import SubjectGrade
from backend.tools.contact import ContactInfo

class Student(Person):
    """
    Class containing the student info.
    """
    def __init__(self, name: str, dob: Date, gender: Gender, contactInfos: List[ContactInfo], id: str, parents: Optional[List[Parent]] = None):
        super().__init__(name, dob, gender, contactInfos, id)
        self.parents = set(parents) if parents else set()


    def __repr__(self, excludeParent = False):
        if (excludeParent):
            return f"<Student><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}</><contactInfos><{self.contactInfos}><id>{self.id}</></>"
        return f"<Student><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}</><contactInfos><{self.contactInfos}><id>{self.id}</></><parents>{self.parents}</></>"

    @lru_cache()
    def ToDataDict(self, excludeVars: Set[str] = {"contactInfos"}) -> dict[str, Any]:
        output = super().ToDataDict()
        dictionary = vars(self)

        for var, value in dictionary.items(): # .items() is cleaner for key/value pairs
            if var in excludeVars:
                continue

            # Handle collection data dict
            if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
                processed_list = []
                for element in value: # Iterate over the original 'value'
                    if hasattr(element, 'ToDataDict'):
                        processed_list.append(element.ToDataDict())
                    else:
                        processed_list.append(element)
                output[var] = processed_list
            else:
                output[var] = value
        
        return output
    


    def AssignToParent(self, parent: Parent):
        return parent.AssignToStudent(self)
    

class StudentGrade:
    """ 
    Class containing the student grade.
    """
    def __init__(self, student: Student, grades: List[SubjectGrade]):
        self.student = student
        self.grades = grades

    def __repr__(self):
        return f"<StudentAge><student>{self.student}<student><grades>{self.grades}</grades></>"
    
    @lru_cache()
    def ToDataDict(self, excludeVars: Set[str] = {"contactInfos"}) -> dict[str, Any]:
        output = {}
        dictionary = vars(self)

        for var, value in dictionary.items(): # .items() is cleaner for key/value pairs
            if var in excludeVars:
                continue

            # Handle collection data dict
            if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
                processed_list = []
                for element in value: # Iterate over the original 'value'
                    if hasattr(element, 'ToDataDict'):
                        processed_list.append(element.ToDataDict())
                    else:
                        processed_list.append(element)
                output[var] = processed_list
            else:
                output[var] = value
        
        return output


class Parent(Person):
    """
    Contains the info of a parent for student.
    """

    def __init__(self, name: str, dob: Date, gender: Gender, id: str, contactInfos: List[ContactInfo], parentOfStudents: List[Student] = []):
        super().__init__(name, dob, gender, contactInfos, id)
        self.parentOfStudents = set(parentOfStudents)

        for student in self.parentOfStudents:
            student.parents.add(self)

    
    def AssignToStudent(self, student: Student):
        """
        Assigns to the children with the given children list on initialise.
        """

        self.parentOfStudents.add(student)
        student.parents.add(self)

        print(f"Assigned parent '{self.name}' to students.")
    

    def RemoveFromStudent(self, student: Student):
        """
        Removes this parent from the student
        """
        self.parentOfStudents.remove(student)
        student.parents.remove(self)
    

    def RemoveFromAll(self):
        """
        Removes this parent from all child
        """
        for student in self.parentOfStudents:
            self.RemoveFromStudent(student)

    @lru_cache()
    def ToDataDict(self, excludeVars: Set[str] = {"student"}) -> dict[str, Any]:
        output = super().ToDataDict(excludeVars)
        dictionary = vars(self)

        for var, value in dictionary.items():
            if var in excludeVars:
                continue

            # Handle collection data dict
            if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
                processed_list = []
                for element in value: # Iterate over the original 'value'
                    if hasattr(element, 'ToDataDict'):
                        processed_list.append(element.ToDataDict())
                    else:
                        processed_list.append(element)
                output[var] = processed_list
            else:
                output[var] = value
        
        return output

    def __repr__(self):
        return f"<Parent><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}><contactInfos><{self.contactInfos}><id>{self.id}</></>"
    
    def GetStudentsStr(self) -> str:
        return f"<parentOfStudents>{self.parentOfStudents}</>"