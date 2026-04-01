"""
Base script for subject.
"""

from student import Student

class Subject:
    """
    Base class for a subject
    """
    def __init__(self, subjectName: str, subjectDescription: str, subjectId: str):
        self.name = subjectName
        self.description = subjectDescription
        self.id = subjectId

    def __str__(self):
        return f"<Subject><name>{self.name}</><description>{self.description}</><id>{self.id}</></>"


class SubjectGrade:
    """
    Contains the subject grade of a student achieves.
    """
    def __init__(self, student: Student, subject: Subject, score: float):
        self.student = student
        self.subject = subject
        self.score = score

    def __str__(self):
        return f"<SubjectGrade><student>{self.student}</><subject>{self.subject}</><score type='float'>{self.score}</></>"