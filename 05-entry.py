#%%
from tkinter import *
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-entry

window = Tk()
window.geometry('300x300')

def sign_in():
    greeting_lbl.config(text=f'sum: {int(first_number.get())+int(second_number.get())}')


Label(window,text='First number: ').pack()
first_number = Entry(window)
first_number.pack()

Label(window,text='Last number: ',).pack()
second_number = Entry(window)
second_number.pack()

Button(window, text='sum',command=sign_in).pack()

greeting_lbl = Label(window)
greeting_lbl.pack()

window.mainloop()
