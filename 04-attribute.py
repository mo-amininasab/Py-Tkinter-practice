#%%
from tkinter import *
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA-%D9%88-%D9%82%D8%A7%D8%A8%D9%84%DB%8C%D8%AA-%D9%87%D8%A7%DB%8C-%D9%87%D8%B1-%D9%88%DB%8C%D8%AF%D8%AC%D8%AA

window = Tk()
window.geometry('500x480')

def change_status():
    status_lable.config(text='status: online', fg= 'green')

status_lable = Label(window, text='status: offline', fg= 'red')
status_lable.pack()

Button(window,text='click me',command=change_status,width=40).pack()




window.mainloop()
