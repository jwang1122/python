from tkinter import filedialog as fd
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('600x400')

def openFile():
    filename = fd.askopenfilename()
    messagebox.showinfo("Selected File", filename)
    
openBtn = tk.Button(root, text='Open a File', command=openFile)
openBtn.pack(side="top")

tk.mainloop()
