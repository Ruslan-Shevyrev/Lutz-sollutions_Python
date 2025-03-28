class Animal:
    def reply(self):
        self.speak()

    def speak(self):
        print('Hello world!')


class Mammal(Animal):
    def speak(self):
        print('Milk')


class Dog(Mammal):
    def speak(self):
        print('Gav')


class Cat(Mammal):
    def speak(self):
        print('Meow')


class Primate(Mammal):
    def speak(self):
        print('Where I am?')


class Hacker(Primate):
    pass
