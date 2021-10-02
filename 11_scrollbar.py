#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/scrollbar
from tkinter import *

window = Tk()
window.geometry('300x300')

scroll = Scrollbar(window)
scroll.pack(side=RIGHT, fill=BOTH)

list_box = Listbox(window)
list_box.pack(expand=True, fill=BOTH)

for line in range(1, 100):
    list_box.insert(END, "this is line number: {}".format(line))

scroll.config(command=list_box.yview)

window.mainloop()
    