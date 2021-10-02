#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%D9%88%DB%8C%D8%AC%D8%AA-%D9%85%D9%86%D9%88
from tkinter import *

window = Tk()
window.geometry('300x300')

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='open')
filemenu.add_command(label='save')
filemenu.add_command(label='exit', command=window.quit)

window.config(menu=menubar)


window.mainloop()
    