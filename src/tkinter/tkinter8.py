import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x300')
my_boolean_var = tk.BooleanVar()

def cmd():
    if my_boolean_var.get():
        print("The check box is selected.")
    else:
        print("The check box is not selected.")

my_checkbutton = ttk.Checkbutton(
    text="Check when selected",
    variable=my_boolean_var,command=cmd
)
my_checkbutton.pack()
root.mainloop()
