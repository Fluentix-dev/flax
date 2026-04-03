"""
Script that defines a person.
"""

from enum import Enum, auto
from .datastructures import Date
from backend.tools.contact import Contact, ContactInfo
from typing import List, Any, Set
from collections.abc import Iterable

class Gender(Enum):
    """
    Enum showing gender.
    """
    Male = 0
    Female = 1



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


    def Contact(self, index: int, msg: str, header: str = ""):
        Contact.Contact(self.contactInfos[index], msg, header)
    

    def __repr__(self):
        return f"<Person><name>{self.name}</><dob>{self.dob}</><gender>{self.gender}><contactInfos><{self.contactInfos}><id>{self.id}</></>"
    

    def ToDataDict(self, excludeVars: Set[str] = {""}) -> dict[str, Any]:
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
    