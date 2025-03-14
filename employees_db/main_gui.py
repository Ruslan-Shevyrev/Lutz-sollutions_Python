import db_handler
from tkinter import *
from tkinter.messagebox import showerror


fields = ('pk', 'name', 'age', 'job', 'pay')
entries = {}


def make_widgets():
    global entries
    window = Tk()
    window.title('Employees')
    form = Frame(window)
    form.pack()

    for ind, field in enumerate(fields):
        label = Label(form, text=field)
        ent = Entry(form)
        label.grid(row=ind, column=0)
        ent.grid(row=ind, column=1)
        entries[field] = ent

    Button(window, text="Fetch", command=fetch_record).pack(side=LEFT)
    Button(window, text="Update", command=update_record).pack(side=LEFT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window


def fetch_record():
    record = db_handler.get_record(entries['pk'].get())
    for field in fields:
        if field != 'pk':
            entries[field].delete(0, END)
            if record is not None:
                entries[field].insert(0, getattr(record, field))


def update_record():
    key = entries['pk'].get()
    record = db_handler.get_record(key)

    if record is None:
        record = db_handler.get_null_record()
    for field in fields:
        setattr(record, field, entries[field].get())
    db_handler.save_record(record)


main_window = make_widgets()
main_window.mainloop()
