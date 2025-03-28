import sys
import traceback


def safe(callee, *pargs, **kargs):
    try:
        callee(*pargs, **kargs)
    except:
        traceback.print_exc()
        print(str(sys.exc_info()[0]) + ' ' + str(sys.exc_info()[1]))


if __name__ == '__main__':
    import try_except

    safe(try_except.oops)
