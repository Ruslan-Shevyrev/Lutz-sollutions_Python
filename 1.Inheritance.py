class Adder:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data

    def __add__(self, x):
        return 'Not Implemented'


class ListAdder(Adder):
    def __add__(self, x):
        return self.data + x


class DictAdder(Adder):
    def __add__(self, x):
        d = self.data.copy()
        d.update(x)
        return d


c = DictAdder({1: 1})

print(c + {2: 2})
