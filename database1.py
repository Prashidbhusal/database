from tkinter import *
import sqlite3

win = Tk()
win.title("databse")

#Database

#creating a database or connect to one

conn = sqlite3.connect("address_book.db")

#creating curser
#curser class in an instance using which you can invoke using method that execute SQLITE,
#fetch data  from result sets of queries
curser = conn.cursor()
#
# #creating the table
# curser.execute("""CREATE TABLE student_data(
#                first_name text,
#                last_name text,
#                address text,
#                city text,
#                state text,
#                zipcode integer
# )
# """)
#
# print("table created sucessfully")
#

#creating function

def submit():
    # creating a database or connect to one

    conn = sqlite3.connect("address_book.db")

    curser = conn.cursor()

    curser.execute("INSERT INTO student_data VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)", {
        'first_name': efirst_name.get(),
        'last_name': elast_name.get(),
        'address': eaddress.get(),
        'city': ecity.get(),
        'state': estate.get(),
        'zipcode': ezipcode.get()
    })
    print('Address inserted successfully')


    conn.commit()

    conn.close()

    efirst_name.delete(0,END)
    elast_name.delete(0,END)
    eaddress.delete(0,END)
    ecity.delete(0,END)
    estate.delete(0,END)
    ezipcode.delete(0,END)


def display():
    conn = sqlite3.connect("address_book.db")

    curser = conn.cursor()
    curser.execute("SELECT *, oid FROM student_data")

    records = curser.fetchall()
    print(records)

    print_records=''

    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(win, text = print_records)
    query_label.grid(row=8,column=0,columnspan=2)

    conn.commit()

    conn.close()


#creating desigh


first_name = Label(win,text="first_name").grid(row=0,column=0)
efirst_name = Entry(win)
efirst_name.grid(row=0, column=1)

last_name = Label(win,text="last_name").grid(row=1,column=0)
elast_name= Entry(win)
elast_name.grid(row=1, column=1)

address = Label(win,text="address").grid(row=2,column=0)
eaddress = Entry(win)
eaddress.grid(row=2, column=1)

city = Label(win,text="city").grid(row=3,column=0)
ecity = Entry(win)
ecity.grid(row=3, column=1)

state = Label(win,text="state").grid(row=4,column=0)
estate = Entry(win)
estate.grid(row=4, column=1)

zipcode = Label(win,text="zipcode").grid(row=5,column=0)
ezipcode= Entry(win)
ezipcode.grid(row=5, column=1)

add_record =  Button(win, text="Addrecords" , command=submit).grid(row=6,columnspan=3)
display =  Button(win, text="Display",command = display ).grid(row=7,columnspan=3)



# commit chnage
conn.commit()

#close connection
conn.close()



mainloop()