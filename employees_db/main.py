import db_handler

db = db_handler.get_db()

bob = db['bob']

print(bob)