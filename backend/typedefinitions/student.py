"""
Base script that defines a student.
"""

from typing import List, Optional
from person import Person, Gender
from datastructures import Date
from subject import SubjectGrade
from ..tools.contact import ContactInfo

class Student(Person):
    """
    Class containing the student info.
    """
    def __init__(self, name: str, dob: Date, gender: Gender, contactInfos: List[ContactInfo], id: str, parents: Optional[List[Parent]] = None):
        super().__init__(name, dob, gender, contactInfos, id)
        self.parents = set(parents) if parents else set()


    def __str__(self):
        return f"<Student><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}><contactInfos><{self.contactInfos}><id>{self.id}</><parents>{self.parents}</></>"

class StudentGrade:
    """
    Class containing the student grade.
    """
    def __init__(self, student: Student, grades: List[SubjectGrade]):
        self.student = student
        self.grades = grades

    def __str__(self):
        return f"<StudentAge><student>{self.student}<student><grades>{self.grades}</grades></>"

class Parent(Person):
    """
    Contains the info of a parent for student.
    """

    def __init__(self, name: str, dob: Date, gender: Gender, id: str, contactInfos: List[ContactInfo], parentOfStudents: List[Student]):
        super().__init__(name, dob, gender, contactInfos, id)
        self.parentOfStudents = set(parentOfStudents)

        self.AssignParentToStudent()

    
    def AssignParentToStudent(self):
        """
        Assigns to the children with the given children list on initialise.
        """
        for student in self.parentOfStudents:
            student.parents.add(self)

        print(f"Assigned parent '{self.name}' to students.")
    

    def RemoveParentFromStudent(self, student: Student):
        """
        Removes this parent from the student
        """
        self.parentOfStudents.remove(student)
        student.parents.remove(self)
    

    def RemoveParentFromAll(self):
        """
        Removes this parent from all child
        """
        for student in self.parentOfStudents:
            self.RemoveParentFromStudent(student)


    def __str__(self):
        return f"<Parent><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}><contactInfos><{self.contactInfos}><id>{self.id}</><parentOfStudents>{self.parentOfStudents}</></>"