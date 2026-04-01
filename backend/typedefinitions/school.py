from classroom import Class
from typing import List

class School:
    def __init__(self, name: str, classes: List[Class], id: str):
        self.name = name
        self.classes = classes
        self.id = id

        # We need a principal
        # and phó hiệu trưởng

        """
        So I have an idea like this

        We have a base Person class
        and each of them will have the following:

        Human stats
        and Role

        All of our jobs will be inherited within the Person class

        Sounds good?
        """