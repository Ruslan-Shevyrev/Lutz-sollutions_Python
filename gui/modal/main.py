from tkinter import *
from tkinter.messagebox import *


def callback():
    if askyesno('Verify', 'Do you really want to quite?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quite has been cancelled')


errmsg = 'Sorry, no spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()