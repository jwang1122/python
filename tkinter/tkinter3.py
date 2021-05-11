import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter")
parent.geometry('600x300')
parent.resizable(0,0)
my_label = tk.Label(parent, text="Hello World!", font=("Arial Bold", 50))
my_label.grid(column=0, row=0)
parent.mainloop()
