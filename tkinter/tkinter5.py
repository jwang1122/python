import tkinter as tk 
parent = tk.Tk() 
parent.geometry('600x300')

canvas_width = 100
canvas_height = 80
w = tk.Canvas(parent, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")
parent.mainloop()
