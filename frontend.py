from tkinter import *
from student import Student
from backend import Database
from major import Major

database = Database("StudentPortal")

class Window():

    """ This class creates the GUI. It pops up to the user, some screens in order to insert and list data """


    def __init__(self, window):
        self.window = window
        self.window.wm_title("Student portal")

        b1 = Button(window, text="Insert student", command=self.add_student)
        b1.grid(row=0, column=0)

        b2 = Button(window, text="List all students", command=self.list_student)
        b2.grid(row=1, column=0)

        b3 = Button(window, text="Insert major", command=self.add_major)
        b3.grid(row=0, column=1)

        b4 = Button(window, text="List all majors", command=self.list_major)
        b4.grid(row=1, column=1)

        b5 = Button(window, text="Insert Major curriculum", command=self.add_curriculum)
        b5.grid(row=0, column=2)

        b6 = Button(window, text="List all major curriculum", command=self.list_curriculum)
        b6.grid(row=1, column=2)

        b7 = Button(window, text="Insert course", command=self.add_course)
        b7.grid(row=0, column=3)

        b8 = Button(window, text="List all courses", command=self.list_course)
        b8.grid(row=1, column=3)

        b9 = Button(window, text="Insert history", command=self.add_history)
        b9.grid(row=0, column=4)

        b10 = Button(window, text="List history", command=self.list_history)
        b10.grid(row=1, column=4)


    def add_student(self):
        window = Toplevel()
        window.wm_title("Student")

        l1 = Label(window, text="ID:")
        l1.grid(row=0, column=0)

        self.id_text = StringVar()
        e1 = Entry(window, textvariable=self.id_text)
        e1.grid(row=0, column=1)

        l2 = Label(window, text="Name:")
        l2.grid(row=1, column=0)

        self.id_name = StringVar()
        e2 = Entry(window, textvariable=self.id_name)
        e2.grid(row=1, column=1)

        b1 = Button(window, text="insert data", command=self.insert_student)
        b1.grid(row=2, column=0)

        window.geometry("500x200")

        window.mainloop()

    def insert_student(self):
        print(self.id_text.get(), self.id_name.get())
        # Student.insertstudent(self.id_text.get(), self.id_name.get())
        student = Student(self.id_text.get(), self.id_name.get())
        student.insertstudent()


    def list_student(self):
        window = Toplevel()
        window.wm_title("Students")

        l1 = Label(window, text="Students list:")
        l1.grid(row=0, column=0, columnspan=6)

        list1 = Listbox(window, height=6, width=35)
        list1.grid(row=1, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        list1.delete(0, END)
        for rows in Student.list_student():
            list1.insert(END, rows)

        window.geometry("500x200")

        window.mainloop()


    def add_major(self):
        window = Toplevel()
        window.wm_title("Major")

        l1 = Label(window, text="Major name:")
        l1.grid(row=0, column=0)

        self.id_text = StringVar()
        e1 = Entry(window, textvariable=self.id_text)
        e1.grid(row=0, column=1)

        b1 = Button(window, text="insert data", command=self.insert_major)
        b1.grid(row=2, column=0)

        b2 = Button(window, text="free fields", command=self.list_major)
        b2.grid(row=2, column=1)

        window.geometry("500x200")

        window.mainloop()

    def insert_major(self):
        major = Major(self.id_text.get())
        major.insert_major()

    def list_major(self):
        window = Toplevel()
        window.wm_title("List all Majors")

        l1 = Label(window, text="Majors list:")
        l1.grid(row=0, column=0, columnspan=6)

        list1 = Listbox(window, height=6, width=35)
        list1.grid(row=1, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        list1.delete(END, 0)
        for rows in Major.list_major():
            list1.insert(END, rows)

        window.geometry("500x200")

        window.mainloop()

    def add_curriculum(self):
        window = Toplevel()
        window.wm_title("Major Curriculum")

        l1 = Label(window, text="Major Curriculum year:")
        l1.grid(row=0, column=0)

        id_text = StringVar()
        e1 = Entry(window, textvariable=id_text)
        e1.grid(row=0, column=1)

        b1 = Button(window, text="insert data", command=self.list_course)
        b1.grid(row=2, column=0)

        b2 = Button(window, text="free fields", command=self.list_course)
        b2.grid(row=2, column=1)

        window.geometry("500x200")



        window.mainloop()

    def list_curriculum(self):
        window = Toplevel()
        window.wm_title("List all Majors Curriculum")

        l1 = Label(window, text="Major curriculum list:")
        l1.grid(row=0, column=0, columnspan=6)

        list1 = Listbox(window, height=6, width=35)
        list1.grid(row=1, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        window.geometry("500x200")

        window.mainloop()

    def add_course(self):
        window = Toplevel()
        window.wm_title("Course")

        l1 = Label(window, text="Insert curse ID:")
        l1.grid(row=0, column=0)

        id_text = StringVar()
        e1 = Entry(window, textvariable=id_text)
        e1.grid(row=0, column=1)
        window.geometry("500x200")

        l2 = Label(window, text="Insert curse Name:")
        l2.grid(row=1, column=0)

        name_text = StringVar()
        e2 = Entry(window, textvariable=name_text)
        e2.grid(row=1, column=1)

        l3 = Label(window, text="Insert hourly load:")
        l3.grid(row=2, column=0)

        hourly_text = StringVar()
        e3 = Entry(window, textvariable=hourly_text)
        e3.grid(row=2, column=1)

        b1 = Button(window, text="insert data", command=self.list_course)
        b1.grid(row=3, column=0)

        b2 = Button(window, text="free fields", command=self.list_course)
        b2.grid(row=3, column=1)


        window.geometry("500x200")


        window.mainloop()


    def list_course(self):
        window = Toplevel()
        window.wm_title("List all courses")

        l1 = Label(window, text="courses list:")
        l1.grid(row=0, column=0, columnspan=6)

        list1 = Listbox(window, height=6, width=35)
        list1.grid(row=1, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        window.geometry("500x200")

        window.mainloop()

    def add_history(self):
        window = Toplevel()
        window.wm_title("Insert course")

        l1 = Label(window, text="Insert curse ID:")
        l1.grid(row=0, column=0)

        id_text = StringVar()
        e1 = Entry(window, textvariable=id_text)
        e1.grid(row=0, column=1)
        window.geometry("500x200")

        l2 = Label(window, text="Insert the year:")
        l2.grid(row=1, column=0)

        year_text = StringVar()
        e2 = Entry(window, textvariable=year_text)
        e2.grid(row=1, column=1)

        l3 = Label(window, text="Insert the semester:")
        l3.grid(row=2, column=0)

        semester_text = StringVar()
        e3 = Entry(window, textvariable=semester_text)
        e3.grid(row=2, column=1)

        l4 = Label(window, text="Insert the grade:")
        l4.grid(row=3, column=0)

        grade_text = StringVar()
        e4 = Entry(window, textvariable=grade_text)
        e4.grid(row=3, column=1)

        b1 = Button(window, text="insert data", command=self.list_course)
        b1.grid(row=4, column=0)

        b2 = Button(window, text="free fields", command=self.list_course)
        b2.grid(row=4, column=1)


        window.geometry("500x200")


        window.mainloop()


    def list_history(self):
        window = Toplevel()
        window.wm_title("List history")

        l1 = Label(window, text="courses list:")
        l1.grid(row=0, column=0, columnspan=6)

        list1 = Listbox(window, height=6, width=35)
        list1.grid(row=1, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        window.geometry("500x200")

        window.mainloop()



window = Tk()

Window(window)

window.geometry("500x200")

window.mainloop()
