import sys


def fn1():
    return 'v0.5'

def fn2():
    print('fn2 called')


if __name__ == '__main__':
    ver = fn1()
    print(ver)
    print('rw')
