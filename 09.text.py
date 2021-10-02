#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/text
from tkinter import *

window = Tk()
window.geometry('300x300')

def save_text():
    print(text.get(1.0, END))
    pass

text = Text(window)
text.pack()

Button(window, text='save', command=save_text).pack()

window.mainloop()
