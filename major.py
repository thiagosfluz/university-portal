from backend import Database

database = Database("StudentPortal")

class Major:

    def __init__(self, name):
        self.name = name



    def insert_major(self):
        database.insert_major(self.name)

    @staticmethod
    def list_major():
        print("HERE"+str(database.view_major()))
        return database.view_major()

