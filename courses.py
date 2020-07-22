from backend import Database

database = Database("StudentPortal")

class Courses:

    def __init__(self, id, year, semester):
        self.id = id
        self.year = year
        self.semester = semester

    def insert_courses(self):
        database.insert_courses(self.id, self.year, self.semester)

    @staticmethod
    def list_courses():
        return database.view_courses()