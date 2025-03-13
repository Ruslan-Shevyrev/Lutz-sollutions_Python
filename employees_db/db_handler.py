import os
import shelve
from person import Person
from manager import Manager

FOLDER = 'db'
DB_NAME = 'class-shelve'
PATH = FOLDER+'/'+DB_NAME


def init():
    bob = Person('Bob Smith', 42, 30000.0, 'software engineer')
    sue = Person('Sue Jones', 40, 40000.0, 'hardware engineer')
    tom = Manager('Tom Doe', 50, 50000.0)

    os.makedirs(FOLDER, exist_ok=True)

    db = shelve.open(PATH)

    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom

    db.close()


def dump():
    db = shelve.open(PATH)
    for key in db:
        print(key, '=>\n ', db[key].name, db[key].pay)


def get_db() -> shelve.open:
    return shelve.open(PATH)