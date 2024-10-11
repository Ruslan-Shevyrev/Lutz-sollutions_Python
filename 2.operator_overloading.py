class MyList:
    def __init__(self, list_in):
        self.list = list(list_in)

    def __add__(self, x):
        return MyList(self.list + x)

    def __mul__(self, x):
        return MyList(self.list * x)

    def __getitem__(self, x, y=None):
        if y==None:
            return self.list[x]
        else:
            return self.list[x:y]

    def __len__(self, x):
        return len(self.list)

    def append(self, x):
        self.list.append(x)

    def __getattr__(self, x):
        return getattr(self.list, x)

    def __repr__(self):
        return repr(self.list)

if __name__ == '__main__':
    x = MyList('test')
    print(x)
    print(x[1])
    print(x[1:3])
    print(x+['list'])
    x.append('a')
    x.sort()
    print(x * 2)
