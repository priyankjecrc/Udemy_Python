## Imp - Go Through it


import sys

## Part1 - Uncomment following and run

'''
import TestModule7

print(sys.modules.keys())  ## TestModule7 --- This is the key in sys.modules
print(globals().keys()) ## TestModule7 --- This is the key in globals()

'''

## Part2 - Uncomment following and run

'''
import TestModule7 as tm7

print(sys.modules.keys()) ## TestModule7 --- This is the key in sys.modules
print(globals().keys())  ## tm7 --- This is the key in globals()

'''

## Part3 - Uncomment following and run

'''
from TestModule7 import printSomething

print(sys.modules.keys()) ## TestModule7 --- This is the key in sys.modules
print(globals().keys()) ## printSomething --- This is the key in globals()

'''

'''
## Part4 - Uncomment following and run

import TestModule7 as tm7
import TestModule7 as tm8

print(sys.modules.keys())  ## TestModule7 --- This is the key in sys.modules
print(globals().keys())  ## 'tm7', 'tm8' ---- This is the key in globals()

'''

## Part4 - Uncomment following and run

'''
import TestModule7.printSomething as ps ## Error - No module named 'TestModule7.printSomething'; 'TestModule7' is not a package

'''

