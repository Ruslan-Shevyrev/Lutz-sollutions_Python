class Attrs:
    def __getattr__(self, item):
        print('get' + item)

    def __setattr__(self, key, value):
        print('set' + key + ' ' + value)
