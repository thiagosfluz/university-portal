from backend import Database
from major import Major

database = Database("StudentPortal")

class Student:

    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major

    def insertstudent(self):
        database.insert_student(self.id, self.name, self.major)

    @staticmethod
    def list_student():
        return database.view_student()
