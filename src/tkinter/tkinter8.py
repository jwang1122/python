"""
using checkbox
"""
from tkinter import *

root = Tk()
root.geometry('600x300')
my_boolean_var = BooleanVar()

def cmd():
    if my_boolean_var.get():
        print("The check box is selected.")
    else:
        print("The check box is not selected.")

my_checkbutton = Checkbutton(
    text="Check when selected",
    variable=my_boolean_var,command=cmd
)
my_checkbutton.pack()
root.mainloop()
