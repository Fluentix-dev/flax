from backend.typedefinitions.school import School
from backend.typedefinitions.classroom import Class, ClassroomType
from backend.typedefinitions.student import Student, Parent
from backend.typedefinitions.datastructures import Date
from backend.typedefinitions.person import Gender
from backend.tools.contact import ContactInfo, ContactChannel


# example data
ngs = School("Newton Grammar School", [], "ngs5")

classrooms = []

nineGC = Class([], [], "9gc", classroomType=ClassroomType.Both)
eightG = Class([], [], "8g", classroomType=ClassroomType.Both)

# nine gc students
lamContacts = [ContactInfo(ContactChannel.Email, "nglamdztop1ff@gmail.com"), ContactInfo(ContactChannel.PhoneNumber, "0123456789")]
lam = Student("Lam", Date(17, 9, 2010), Gender.Male, lamContacts, "lam12345")

lamDadContacts = [ContactInfo(ContactChannel.Email, "abc@gmail.com")]
lamDad = Parent("John", Date(1, 1, 1989), Gender.Male, "lamDad12345", lamDadContacts)
lamDad.AssignToStudent(lam)

nineGC.AddStudent(lam)

print(lam.ToDataDict())

print("Done setting up test data!")

# export
