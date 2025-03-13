from person import Person


class Manager(Person):
    def give_raise(self, percent: float, bonus: float = 0.1):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    tom = Manager('Tom Doe', 50, 50000, 'software engineer')
    print(tom)
    print(tom.last_name())
    print('Tom\'s pay before raise: ' + str(tom.pay))
    tom.give_raise(.10)
    print('Tom\'s pay after raise: ' + str(tom.pay))
