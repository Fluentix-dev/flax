"""
Generic script that contains extra data structures.
"""

from datetime import date

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
    
    
    def __str__(self):
        return f"<Date><day>{self.day}</><month>{self.month}</><year>{self.year}</></>"