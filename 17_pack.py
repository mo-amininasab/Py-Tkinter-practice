#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D8%A7%DB%8C%D8%AC%D8%A7%D8%AF-%D8%B3%D8%A7%D8%AE%D8%AA%D8%A7%D8%B1-%D8%A8%D8%A7-pack
from tkinter import *

window = Tk()
window.geometry('300x300')

Frame(window, bg='yellow').pack(expand=True, fill=BOTH, side=TOP)

bottom_frame = Frame(window)
bottom_frame.pack(expand=True, fill=BOTH)


Frame(bottom_frame, bg='blue').pack(expand=True, fill=BOTH, side=LEFT)
Frame(bottom_frame, bg='red').pack(expand=True, fill=BOTH, side=LEFT)
Frame(bottom_frame, bg='green').pack(expand=True, fill=BOTH, side=LEFT)

window.mainloop()
    