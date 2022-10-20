
import sys

print(sys.modules.keys())
print(globals().keys())



__all__ = ['module12Func1']


def module12Func1():
    print('This is module12 1st Function')


def module12Func2():
    print('This is module12 2nd Function')


def module12Func3():
    print('This is module12 3rd Function')


print(sys.modules.keys())
print(globals().keys())