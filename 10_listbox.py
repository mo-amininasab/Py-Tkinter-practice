#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D8%B3%D8%A7%D8%AE%D8%AA-%DB%8C%DA%A9-list-box
from tkinter import *

window = Tk()
window.geometry('300x300')

names = Entry(window)
names.pack()

def add_name():
    my_list.insert(END ,names.get())

Button(window, text="add name", command=add_name).pack()

my_list = Listbox(window) 
my_list.pack()

def clear_list():
    my_list.delete(0, END)

Button(window, text="clear", command=clear_list).pack()

my_list.insert(1, "ali")
my_list.insert(2, "mohammad")
my_list.insert(3, "sarin")

window.mainloop()
    