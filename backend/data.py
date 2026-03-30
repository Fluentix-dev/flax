from __future__ import annotations
from typing import List, Optional
from datetime import date
from enum import Enum, auto
from tools.contact import Contact, ContactInfo


class Gender(Enum):
    Male = auto()
    Female = auto()

class Date:
    def __init__(self, d: int, m: int, y: int):
        self.day = d
        self.month = m
        self.year = y
    
    def CurrentAge(self) -> float:
        now = date.today()

        birth_date = date(self.year, self.month, self.day)
        age = now - birth_date

        return age.days / 365.25
    
    def IsBirthdayToday(self) -> bool:
        now = date.today()
        return now.day == self.day and now.month == self.month

    def IsBirthday(self, date: Date) -> bool:
        return date.day == self.day and date.month == self.month

class Person:
    """
    Base class for a person.
    """
    def __init__(self, name: str, dob: Date, gender: Gender, contactInfos: List[ContactInfo], id: str):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.contactInfos = contactInfos
        self.id = id

    def Contact(self, index: int):
        Contact.Contact(self.contactInfos[index])


class Parent(Person):
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


class Student(Person):
    """
    Class containing the student info.
    """
    def __init__(self, name: str, dob: Date, gender: Gender, contactInfos: List[ContactInfo], id: str, parents: Optional[List[Parent]] = None):
        super().__init__(name, dob, gender, contactInfos, id)
        self.parents = set(parents) if parents else set()


class StudentGrade:
    def __init__(self, student: Student, grades: StudentGrade):
        self.student = student
        self.grades = grades


class Subject:
    def __init__(self, subjectName: str, subjectDescription: str, subjectId: str):
        self.name = subjectName
        self.description = subjectDescription
        self.id = subjectId


class SubjectGrade:
    def __init__(self, subject: Subject, score: float):
        self.subject = subject
        self.score = score


class Role:
    def __init__(self, roleName: str, roleDescription: str, roleId: str):
        self.name = roleName
        self.description = roleDescription
        self.id = roleId


class Class:
    """
    A class containing all the students, teachers.
    """
    def __init__(self, students: List[Student]):
        self.Students = []
        self.Teachers = []