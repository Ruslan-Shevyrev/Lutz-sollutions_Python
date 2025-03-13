import db_handler

db_handler.init()

bob = db_handler.get_record('bob')

print(bob.pay)

bob.give_raise(0.1)

print(bob.pay)

db_handler.save_record(bob)

db_handler.dump()
