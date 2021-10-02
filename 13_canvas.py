#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-canvas
from tkinter import *

window = Tk()
window.geometry('300x300')

canvas_window = Canvas(window,width=500, height=300)
canvas_window.pack()

canvas_window.create_line(10, 20, 30, 100, fill='red', dash=(4,4))

canvas_window.create_rectangle(100, 20, 200, 100, fill='blue')

window.mainloop()
    