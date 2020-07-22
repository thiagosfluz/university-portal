import sqlite3

list_ = ['a', 'b', 'c']

#create a data structure
conn = sqlite3.connect('example.db')
c = conn.cursor()

#Create table
c.execute('''Create TABLE if not exists server("sites")''')

#Insert links into table
def data_entry():
    for item in list_:
        c.execute("INSERT INTO server(sites) VALUES(?)", (item))
    conn.commit()

data_entry()  # ==> call the function

#query database
c.execute("SELECT * FROM server")
rows = c.fetchall()
for row in rows:
    print(row)


conn.close()