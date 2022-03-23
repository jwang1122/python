import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("300x200+300+300")
root.title("Using Frame")

frame = tk.Frame(root, bg='#00FFFF')
tk.Label(frame, text='Hello, the world!').pack(pady=10)
tk.Button(frame, text="Do nothing").pack(pady=10)
frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=1)

root.mainloop()