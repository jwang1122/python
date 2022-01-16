from PIL import Image, ImageTk
from itertools import count, cycle
import tkinter as tk
 
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 
#demo :
root = tk.Tk()
lbl1 = ImageLabel(root)
lbl1.pack()
lbl1.load('images/workForLive.gif')
lbl2 = ImageLabel(root)
lbl2.pack()
lbl2.load('images/happyHoliday.gif')
lbl3 = ImageLabel(root)
lbl3.pack()
lbl3.load('images/familyguy.gif')
lbl4 = ImageLabel(root)
lbl4.pack()
lbl4.load('images/beVegan.gif')
root.mainloop()