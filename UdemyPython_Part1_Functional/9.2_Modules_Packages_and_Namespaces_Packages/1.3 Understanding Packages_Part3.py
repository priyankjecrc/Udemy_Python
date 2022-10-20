## We are referencing to Package3 ....  It has Module1.py, Module2.py, Module3.py and __init__.py.. ie 3 module files in it

## IMP -
## Understanding use of __all__

## Whatever list we define in __all__, will replace *
## Better to understand in this way.. Suppose in a file there are many functions..But when somebody wants to import everything from
## that file (using *) and we want to limit that, then we can use __all__..By mentioning limited functions in __all__ , only the
## mentioned functions will be allowed to import


import sys


## Case 1 ... for eg we have defined __all__ in init.py of Package3 as ----> __all__ = ['Module1','Module2']

'''
from Package3 import *  ## It will mean here... from Package3 import Module1, Module2


print(sys.modules.keys())  ## 'Package3', 'Package3.Module1', 'Package3.Module2' ... are keys
print(globals().keys())  ## 'Module1', 'Module2' are keys

Module1.printSomething1() ## will work as expected
Module1.printSomething2() ## will work as expected
Module2.sampleFunc() ## will work as expected

'''

## Case 2 ... While doing ... from Package3.Module1 import * ... we just want printSomething1 to be imported

'''

from Package3.Module1 import *  ## will be equivalent to from Package3.Module1 import printSomething1

printSomething1()
## printSomething2() ... this will not work

'''