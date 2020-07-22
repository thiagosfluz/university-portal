from backend import Database

database = Database("StudentPortal")

class Major:

    def __init__(self, id, name, courses):
        self.id = id
        self.name = name
        self.courses = courses



    def insert_major(self):
        database.insert_major(self.id, self.name, self.courses)

    @staticmethod
    def list_major():
        return database.view_major()

