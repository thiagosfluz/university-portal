from backend import Database

database = Database("StudentPortal")

class Courses:

    def __init__(self, year, semester):
        self.year = year
        self.semester = semester

    def insert_courses(self):
        database.insert_courses(self.name)

    @staticmethod
    def list_courses():
        return database.view_courses()