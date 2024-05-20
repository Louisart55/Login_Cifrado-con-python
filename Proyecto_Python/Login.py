from tkinter import*
import tkinter.messagebox
import csv

def Login():
    e1 = Entry1.get()
    e2 = Entry2.get()

    if e1 == "" or e2 == "":
        tkinter.messagebox.showinfo('Error', 'Enter all the values in!')
    else:
        x = 0
        with open('Usuarios.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if x == 0:
                    for field in row:
                        if field == e1 and row[1] == e2 and x==0:
                            tkinter.messagebox.showinfo('Login', 'Logged in Successfully')
                            x = 1
                            break


top = Tk()
top.geometry("300x300")
Button1 = Button(text="Submit", command=Login)
Button1.place(x=130, y=200)
text1 = Label(top, text="Username:")
text1.place(x=50, y= 80)
text2 = Label(top, text="Password:")
text2.place(x=50, y= 140)
Entry1 = Entry(top)
Entry1.place(x=125, y=82)
Entry2 = Entry(top)
Entry2.place(x=125, y=142)
top.mainloop()