import tkinter as tk 
parent = tk.Tk() 
parent.title('Title - button') 
parent.geometry('600x300')
my_button = tk.Button(parent, text='Quit', height=1, width=20, command=parent.destroy) 
my_button.pack() 
parent.mainloop()
