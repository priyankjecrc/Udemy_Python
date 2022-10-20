
## We are referencing to Package1... It has Module1.py, Module2.py, Module3.py and __init__.py.. ie 3 module files in it
##                                   and InnerPackage with __init__.py and InnerModule.py module file

## IMP -

## 1. When we import a Package, the modules and packages present in it DOESN'T get automatically imported
## 2. We will have to import each module or package present in package explicitly
## 3. __init__.py file inside Package gets automaticaly executed when we import Package
## 4. When doing import for eg as import Package1.Package2.Package3.someModule.. in globals() only Package1 will go as key
## 5. When doing something lile -- from Package1.somemodule import * ... all the variables that start with '_' or with '__' will not be imported

import sys




## Before starting actual, we will like to look into this problem
## Very Imp Problem --- I can't Iterate over globals().keys() in following way

'''
print(globals().keys())  ## dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtin__', '__builtins__', '_ih', '_oh', '_dh', 'In', 'Out', 'get_ipython', 'exit', 'quit', '_', '__', '___', '_i', '_ii', '_iii', '_i1', 'sys', '_i2', '__file__'])


for k in globals().keys():
    print(globals().keys())  ## dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtin__', '__builtins__', '_ih', '_oh', '_dh', 'In', 'Out', 'get_ipython', 'exit', 'quit', '_', '__', '___', '_i', '_ii', '_iii', '_i1', 'sys', '_i2', '__file__', 'k'])

    print(k)                   ## Error: RuntimeError: dictionary changed size during iteration
                               ## But Why... 
                               ## lets assume that globals().keys() give values as 'one', 'two', 'three'
                               ## now k will be = 'one'...Now before start of iteration 'k' was not in globals(). Now 'k' will be added as key in globals()
                               ## hence we are changing size of global() while iterating.
                               ## we can change value of key of dictionary during iteration, but we cant change size of dictionary

'''


## Trial 1

'''
import Package1

print(sys.modules.keys()) ## 'Package1' will be present as key
print(globals().keys()) ## 'Package1' will be present as key

Package1.Module1 ## This will not work..

'''

## Trial 2 ... IMP

'''
import Package1.Module1

print(sys.modules.keys()) ## 'Package1', 'Package1.Module1' ... will be present as key
print(globals().keys()) ## 'Package1' .. only this will be present as key
                        ## Python will only add very first in globals  ........................IMP

## Module1.printSomething1() .. will not work. We will have to give full path
Package1.Module1.printSomething1() ## This will work

'''

## Trial 3

'''
import Package1.Module1 as md1

print(sys.modules.keys()) ## 'Package1', 'Package1.Module1' ... will be present as key
print(globals().keys()) ## 'md1' will be present as key. Infact 'md1' will be pointing to 'Package1.Module1'

print(id(globals()['md1']))                  ## 1907985982632
print(id(sys.modules['Package1.Module1']))   ## 1907985982632  ... both are same..confirms that  'md1' points to 'Package1.Module1'

md1.printSomething1() ## This will work as 'md1' means 'Package1.Module1'

'''

## Trial 4

'''
from Package1 import Module1 

print(sys.modules.keys()) ## 'Package1', 'Package1.Module1' ... will be present as key
print(globals().keys())  ## 'Module1' will be present as key

Module1.printSomething1() ## Will work as expected

'''

## Trial 5

'''
from Package1.Module1 import printSomething1

print(sys.modules.keys()) ## 'Package1', 'Package1.Module1' ... will be present as key
print(globals().keys()) ## 'printSomething1' .. .will be present as key

printSomething1() ## Will work as expected

'''

## Trial 6

'''

from Package1 import *   ## This will not import modules automatically

print(sys.modules.keys())  ## 'Package1' will be present as key
print(globals().keys()) ## 'Package1', will not be there..

'''


## Trial 7

'''

from Package1.Module1 import * 

print(sys.modules.keys()) ## 'Package1', 'Package1.Module1' ... will be present as key
print(globals().keys()) ## 'printSomething1' will be present as key

'''

## Trial 8

'''
import Package1.InnerPackage.InnerModule

print(sys.modules.keys()) ##  'Package1', 'Package1.InnerPackage', 'Package1.InnerPackage.InnerModule' will be keys
print(globals().keys()) ## 'Package1' is the key.... something to notice

'''