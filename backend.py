import sqlite3
from tkinter import *

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS major (id INT PRIMARY KEY not null, name text not null, courses_id text not null, FOREIGN KEY (courses_id) references courses (id))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS student (id INT PRIMARY KEY not null, name text not null, major_name text not null, "
                         "FOREIGN KEY (major_name) references major (name))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS courses (id INT PRIMARY KEY not null, year integer not null, semester integer not null)")
        self.conn.commit()

    def insert_student(self, id, name, major_name):
        try:
            self.cur.execute("INSERT INTO student VALUES (?, ?, ?)", (id, name, major_name))
            self.conn.commit()
            self.alert_popup("Success", "The student was recorded!")
            print("Success")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_student(self):
        self.cur.execute("SELECT * FROM student")
        rows = self.cur.fetchall()
        print("Imprimindo ROWS" + str(rows))
        return rows

    def insert_major(self, id, name, courses_id):
        try:
            self.cur.execute("INSERT INTO major VALUES (?, ?, ?)", (id, name, courses_id))
            self.conn.commit()
            self.alert_popup("Success", "The major was recorded!")
            print("Sucess")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_major(self):
        self.cur.execute("SELECT name FROM major")
        rows = self.cur.fetchall()
        return rows

    def insert_courses(self, name):
        try:
            self.cur.execute("INSERT INTO major VALUES (?)", (name,))
            self.conn.commit()
            self.alert_popup("Success", "The major was recorded!")
            print("Sucess")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_courses(self):
        self.cur.execute("SELECT * FROM courses")
        rows = self.cur.fetchall()
        return rows

    def alert_popup(self, title, message):
        """Generate a pop-up window for special messages."""
        root = Tk()
        root.title(title)
        w = 400  # popup window width
        h = 200  # popup window height
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        m = message
        m += '\n'
        w = Label(root, text=m, width=120, height=10)
        w.pack()
        b = Button(root, text="OK", command=root.destroy, width=10)
        b.pack()
        mainloop()


