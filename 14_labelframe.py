#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/label-frame
from tkinter import *

window = Tk()
window.geometry('300x300')

frame_1 = LabelFrame(window, text='registration')
frame_1.pack(fill=BOTH, expand=True)


frame_2 = Frame(window, bg='white')
frame_2.pack(fill=BOTH, expand=True)

frame_3 = Frame(window, bg='red')
frame_3.pack(fill=BOTH, expand=True)

Label(frame_1, text='label in frame 1').pack()
Label(frame_2, text='label in frame 2').pack()



window.mainloop()
    