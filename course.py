from backend import Database

database = Database("StudentPortal")

class Course:

    def __init__(self, id, name, duration):
        self.id = id
        self.name = name
        self.duration = duration

    def insert_course(self):
        database.insert_course(self.id, self.name, self.duration)

    @staticmethod
    def list_course():
        return database.view_course()
