from backend import Database

database = Database("StudentPortal")

class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def insertstudent(self):
        database.insert_student(self.id, self.name)

    @staticmethod
    def list_student():
        return database.view_student()
