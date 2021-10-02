#%%
from tkinter import *

window = Tk()
window.geometry('300x300')

Label(window, text='test1', bg='green').grid(row=0, column=0)
Label(window, text='test222222', bg='red').grid(row=1, column=1)
Label(window, text='test3', bg='yellow').grid(row=0, column=2)


window.mainloop()
    