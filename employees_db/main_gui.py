import db_handler
from tkinter import *

fields = ('pk', 'name', 'age', 'job', 'pay')
entries = {}


def create_main_window():
    global entries
    window = Tk()
    window.geometry("400x150")
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
    Button(window, text="Show all keys", command=all_keys_window).pack(side=RIGHT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window


def dismiss(window):
    window.grab_release()
    window.destroy()


def all_keys_window():
    window = Toplevel()
    window.geometry("400x150")
    window.title('All keys')
    Button(window, text="Close", command=lambda: dismiss(window)).pack(side=RIGHT)
    window.grab_set()
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


main_window = create_main_window()
main_window.mainloop()
