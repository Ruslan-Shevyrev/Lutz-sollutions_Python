import os
import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000.0, 'software engineer')
sue = Person('Sue Jones', 40, 40000.0, 'hardware engineer')
tom = Manager('Tom Doe', 50, 50000.0)

os.makedirs('db', exist_ok=True)

db = shelve.open('db/class-shelve')

db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

db.close()
