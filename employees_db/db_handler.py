import os
import shelve
from person import Person
from manager import Manager

FOLDER = 'db'
DB_NAME = 'class-shelve'
PATH = FOLDER + '/' + DB_NAME


def init():
    records = [Person('bob', 'Bob Smith', 42, 30000.0, 'software engineer'),

               Person('sue', 'Sue Jones', 40, 40000.0, 'hardware engineer'),

               Manager('tom', 'Tom Doe', 50, 50000.0)]

    os.makedirs(FOLDER, exist_ok=True)

    db = shelve.open(PATH)

    for record in records:
        db[record.pk] = record

    db.close()


def dump():
    db = shelve.open(PATH)
    for key in db:
        print(key, '=>\n ', db[key].name, db[key].pay)


def get_keys():
    db = shelve.open(PATH)
    keys = [db[key].pk for key in db]
    return keys

def get_db() -> shelve.open:
    return shelve.open(PATH)


def get_record(key: str) -> Person | None:
    try:
        return shelve.open(PATH)[key]
    except KeyError:
        return None


def save_record(record: Person):
    db = shelve.open(PATH)

    db[record.pk] = record

    db.close()


def get_null_record() -> Person:
    return Person(pk='', name='', age=0, job='', pay=0.0)
