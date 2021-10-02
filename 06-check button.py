#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D8%B3%D8%A7%D8%AE%D8%AA-checkbuttonfrom tkinter import *

from tkinter import *

window = Tk()
window.geometry('300x300')

def get_state():
    if male_var.get() == 1:
        print('do silent mode')
    else:
        print('do regular mode')

male_var = IntVar()     # for getting value from Checkbutton, we have to define a varialbe
Checkbutton(window, text='male',variable=male_var).pack()

Button(window, text='show state', command= get_state).pack()


window.mainloop()
