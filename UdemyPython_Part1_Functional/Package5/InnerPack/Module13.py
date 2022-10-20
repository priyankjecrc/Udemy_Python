import sys

print(sys.modules.keys())
print(globals().keys())



__all__ = ['module13Func1']


def module13Func1():
    print('This is module13 1st Function')


def module13Func2():
    print('This is module13 2nd Function')


def module13Func3():
    print('This is module13 3rd Function')

print(sys.modules.keys())
print(globals().keys())