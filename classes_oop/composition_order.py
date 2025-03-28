class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food_name):
        self.customer.place_order(food_name, self.employee)

    def result(self):
        return self.customer.print_food()


class Customer:
    def __init__(self):
        self.food = None

    def place_order(self, food_name, employee):
        self.food = employee.take_order(food_name)

    def print_food(self):
        print(self.food.name)


class Employee:
    @staticmethod
    def take_order(food_name):
        return Food(food_name)


class Food:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    x = Lunch()
    x.order('Pizza')
    x.result()

    x.order('Soup')
    x.result()
