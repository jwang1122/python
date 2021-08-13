"""
using grid system
change font of the label
"""
import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter")
parent.geometry('600x300')
parent.resizable(0,0)
myLabel1 = tk.Label(parent, text="Hello World!", font=("Arial Bold", 50))
myLabel1.grid(column=0, row=0)
myLabel2 = tk.Label(parent, text="My name is John Wang.",font=("Bradley Hand ITC", 30))
myLabel2.grid(column=0, row=1)
parent.mainloop()
