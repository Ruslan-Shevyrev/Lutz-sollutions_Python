def oops():
    raise IndexError


def oops_2():
    try:
        oops()
    except IndexError:
        print('IndexError')


if __name__ == '__main__':
    oops_2()
