from tkinter import *
from gui.modules.dialog_table import demos
from gui.modules.Quitter import Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, options)
        self.pack()
        Label(self, text="Basic demos").pack()
        for key in demos:
            func = (lambda key=key: self.printin(key))
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def printin(self, name):
        print(name, 'returns =>', demos[name]())


if __name__ == '__main__':
    demo = Demo()
    demo.mainloop()

