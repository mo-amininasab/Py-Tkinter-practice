#%%
from tkinter import *

window = Tk()
window.geometry('500x480')

Label(window,text='static').pack()  # it is static

hello_lable = Label(window, text = 'dynamic')   # its dynamic(Objective) and can change
hello_lable.pack()

hello_lable.config(fg = 'red')    # can comes after or before the pack

window.mainloop()
