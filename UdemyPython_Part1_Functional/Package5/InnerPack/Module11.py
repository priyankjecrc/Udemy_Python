import sys

print(sys.modules.keys())
print(globals().keys())

__all__ = ['module11Func1']

def module11Func1():
    print('This is module11 1st Function')


def module11Func2():
    print('This is module11 2nd Function')

def module11Func3():
    print('This is module11 3rd Function')

print(sys.modules.keys())
print(globals().keys())