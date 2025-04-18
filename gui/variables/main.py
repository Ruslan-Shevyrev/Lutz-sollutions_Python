from tkinter import *

root = Tk()
states = []


def show():
    for state in states:
        print(state.get())


for i in range(10):
    var = IntVar()
    chk = Checkbutton(root, text=str(i), variable=var)
    chk.pack()
    states.append(var)


Button(root, text='Show', command=show).pack(fill=X)

root.mainloop()
