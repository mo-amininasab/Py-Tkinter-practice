#%%
from tkinter import *

counter = 0
def print_hello():
    global counter
    counter += 1
    hello_cnt.config(text=f'count: {counter}')

window = Tk()
window.geometry('500x480')

hello_cnt = Label(window, text='count: ')
hello_cnt.pack()

Button(window,text='click me',command=print_hello).pack()



window.mainloop()
