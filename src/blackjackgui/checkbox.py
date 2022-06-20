from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Check Box")
isSelected1 = BooleanVar() # not a good variable naming
isSelected2 = BooleanVar()

def select1():
    flag = isSelected1.get() 
    if flag:
        print("1 is selected.")
    else:
        print("1 is NOT selected.")

def select2():
    flag = isSelected2.get()
    if flag:
        print("2 is selected.")
    else:
        print("2 is NOT selected.")

Checkbutton(text="Red", variable=isSelected1, command=select1).pack()
Checkbutton(text="Blue", variable=isSelected2, command=select2).pack()
root.mainloop()
