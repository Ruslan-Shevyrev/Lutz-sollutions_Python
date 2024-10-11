class Adder:
    def add(self, x, y):
        return 'Not Implemented'

    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def __add__(self, arg):
        return self.add(self.data, arg)


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        d = {}
        for i in x.keys(): d[i] = x[i]
        for i in y.keys(): d[i] = y[i]
        return d


c = DictAdder()

print(c.add({1:1}, {2:2}))
