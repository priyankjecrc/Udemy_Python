## Read all the theory in 01_WhatIsModule.py.. We can watch video 130 must most of the stuff is not required

import math
print(math)  ## <module 'math' (built-in)> ... this is built in

import fractions
print(fractions) ## <module 'fractions' from 'C:\\Users\\japr01\\Anaconda3\\envs\\UdemyPython_Part1_Functional\\lib\\fractions.py'>
                 ## This is actually giving location to actual file

import sys

import TestModule    ##  This is TestModule
del globals()['TestModule']  ## We are deleting reference just from globals. It means that it is still there in sys.modules

TestModule.printName()  ## NameError: name 'TestModule' is not defined... because we have deleted TestModule from name space.
                        ## We will have to import TestModule again to make it work