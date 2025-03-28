class MyError(Exception):
    pass


def oops():
    raise MyError('Test')


def oops_2():
    try:
        oops()
    except IndexError:
        print('IndexError')
    except MyError as error:
        print('MyError ', MyError, error)


if __name__ == '__main__':
    oops_2()
