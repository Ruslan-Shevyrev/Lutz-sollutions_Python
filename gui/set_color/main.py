from tkinter import *
from tkinter.colorchooser import askcolor


def set_bg_color():
    (triple, hex_str) = askcolor()
    if hex_str:
        print(hex_str)
        push.config(bg=hex_str)


def on_left_click(event):
    print('Left Click')


root = Tk()
push = Button(root, text='Set bg color', command=set_bg_color)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.bind('<Button-1>', on_left_click)
root.mainloop()
