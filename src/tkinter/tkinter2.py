"""
Add label to window
"""
import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter")
parent.geometry('600x300')

myLabel = tk.Label(parent, text="Label widget")
# myLabel.grid(column=0, row=0) # put label on location (9,0)
myLabel.pack()
parent.mainloop()
