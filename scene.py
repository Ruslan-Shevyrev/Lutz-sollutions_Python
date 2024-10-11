class Actor:
    name = None

    def says(self):
        return None

    def line(self):
        print(self.name + ': ' + repr(self.says()))


class Customer(Actor):
    name = 'customer'

    def says(self):
        return "that's one ex-bird!"


class Clerk(Actor):
    name = 'customer'

    def says(self):
        return "Customer: no it isn't"


class Parrot(Actor):
    name = 'parrot'


class Scene():
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()


if __name__ == '__main__':
    scene = Scene()
    scene.action()
