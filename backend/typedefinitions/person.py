"""
Script that defines a person.
"""

from enum import Enum, auto
from datastructures import Date
from ..tools.contact import Contact, ContactInfo
from typing import List

class Gender(Enum):
    """
    Enum showing gender.
    """
    Male = auto()
    Female = auto()

    def __str__(self):
        return f"<Gender>{self.name}</>"


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
    
    def __str__(self):
        return f"<Person><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}><contactInfos><{self.contactInfos}><id>{self.id}</></>"
    