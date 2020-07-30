from backend import Database

database = Database("StudentPortal")

class Courses:

    def __init__(self, id, year, semester, course1, course2):
        self.id = id
        self.year = year
        self.semester = semester
        self.course1 = course1
        self.course2 = course2

    def insert_courses(self):
        database.insert_courses(self.id, self.year, self.semester, self.course1, self.course2)

    @staticmethod
    def list_courses():
        return database.view_courses()