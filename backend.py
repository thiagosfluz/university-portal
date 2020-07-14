import sqlite3
from tkinter import *

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS student (id INT PRIMARY KEY not null, name text not null)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS major (name text not null)")
        self.conn.commit()

    def insert_student(self, id, name):
        try:
            self.cur.execute("INSERT INTO student VALUES (?, ?)", (id, name))
            self.conn.commit()
            self.alert_popup("Success", "The student was recorded!")
            print("Sucess")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_student(self):
        self.cur.execute("SELECT * FROM student")
        rows = self.cur.fetchall()
        return rows

    def insert_major(self, name):
        try:
            self.cur.execute("INSERT INTO major VALUES (?)", (name,))
            self.conn.commit()
            self.alert_popup("Success", "The major was recorded!")
            print("Sucess")
        except:
            self.alert_popup("Try again", "ERROR")

    def view_major(self):
        self.cur.execute("SELECT * FROM major")
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

