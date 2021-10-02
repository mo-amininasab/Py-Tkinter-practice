#%%
# https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/paned-window
from tkinter import *

window = Tk()
window.geometry('300x300')

pannel_1 = PanedWindow(window, bg='red', bd=4)
pannel_1.pack(fill=BOTH, expand=True)

label_pnl_1 = Label(pannel_1, text='pannel 1')
pannel_1.add(label_pnl_1)

pannel_2 = PanedWindow(window, bg='blue', bd=4, orient=VERTICAL)
pannel_1.add(pannel_2)

label_pnl_2 = Label(pannel_2, text='pannel 2')
pannel_2.add(label_pnl_2)
pannel_2.add(Label(pannel_2, text='test'))

window.mainloop()
    