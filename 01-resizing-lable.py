#%%
from tkinter import *

window = Tk()
# window size
window.title('Hello World!')
window.minsize(400,300)     # min size
window.maxsize(640,450)     # max size
window.geometry('500x480')  # default size
window.resizable(width = False, height= True)

# lable
Label(window,text = 'Hello World1!',font = 'times').pack()
Label(window,text = 'Hello World2!', font = ('tahoma',50)).pack()
Label(window,text = 'Hello World3!', fg='red', bg='blue').pack()

# button
Button(window,text = 'click me',bg = 'yellow').pack()

window.mainloop()




