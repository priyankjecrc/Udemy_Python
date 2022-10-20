print('This is Module1')

## Now suppose when doing * on this file, I want on printSomething1 to be exported

__all__ = ['printSomething1']

def printSomething1():
    print('inside Module1 printSomething1')

def printSomething2():
    print('inside Module1 printSomething2')

def printSomething3():
    print('inside Module1 printSomething3')


