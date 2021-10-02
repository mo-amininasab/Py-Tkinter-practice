#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/messagebox
from tkinter import *
from tkinter import messagebox

def show_info():
    messagebox.showinfo('author', 'written by alibigdeli')
def show_error():
    messagebox.showerror('ERROR', 'somthing happend')
def show_warning():
    messagebox.showwarning('warning', 'your data will be loss')
def show_ask():
    messagebox.askquestion('q/a', 'Wanna exit?')
    # messagebox.askokcancel('q/a', 'Wanna exit?')
    # messagebox.askyesno('q/a', 'Wanna exit?')
    # messagebox.askretrycancel('q/a', 'Wanna exit?')
    pass

window = Tk()
window.geometry('300x300')

menubar = Menu(window)
menubar.add_command(label='info', command=show_info)
menubar.add_command(label='exit', command=show_ask)

window.config(menu=menubar)

Button(window, text='warning', command=show_warning).pack()
Button(window, text='error', command=show_error).pack()
window.mainloop()
    