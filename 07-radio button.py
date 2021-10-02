#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/radio-button
from tkinter import *

window = Tk()
window.geometry('300x300')

Modes = [('male','male'),('female','female'),('not to metion','not to mention')]    # ('name', 'value')

choice = StringVar()
choice.set('male')  #   value = 'male' not name = 'male'

for text, mode in Modes:
    Radiobutton(window,text=text, variable=choice, value=mode).pack()


window.mainloop()
