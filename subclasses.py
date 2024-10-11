from operator_overloading import MyList


class MyListSub(MyList):

    calls = 0

    def __init__(self, list_in):
        self.stdout = 0
        MyList.__init__(self, list_in)

    def __add__(self, x):
        self.stdout += 1
        MyListSub.calls += 1
        print('stdout = ' + str(self.stdout))
        return MyList.__add__(self, x)

    def stats(self):
        return self.stdout, self.calls


if __name__ == '__main__':
    x = MyListSub('test1')
    y = MyListSub('test2')
    print(x + ['1'])
    print(x + ['12'])
    print(y + ['12'])
    print(x.stats())
    print(y.stats())
