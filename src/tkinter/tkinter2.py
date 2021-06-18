import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter")
parent.geometry('600x300')
my_label = tk.Label(parent, text="Label widget")
my_label.grid(column=0, row=0)
parent.mainloop()
