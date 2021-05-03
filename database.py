from tkinter import *
import sqlite3

root = Tk()
root.title('Database Address Book')
#database
#creating a database or connection one
conn = sqlite3.connect('address_book.db')

#creating cursor
#cursor class is an instance using which you can invoke mathod that
#execute SQLITE,statements, fetch data from result sets of the queries
c = conn.cursor()

#creat table
c.execute("""CREATE TABLE addresses(
         first_name text,
         last_name text,
         address text,
         city text,
         state text,
         zipcode integer
)""")

print("Table created successfully")

#commit change
conn.commit()

#close connection
conn.close()

mainloop()

