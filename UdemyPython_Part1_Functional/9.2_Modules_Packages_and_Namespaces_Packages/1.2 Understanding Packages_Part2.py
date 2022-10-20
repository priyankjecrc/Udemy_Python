## We are referencing to Package2... It has Module1.py, Module2.py, Module3.py and __init__.py.. ie 3 module files in it
##                                   and InnerPackage with __init__.py and InnerModule.py module file
##                                   We havent used Module 1,2,3 files



## Case 1

'''

## To access innerfunc1 which is present in InnerModule fie we have to import entire thing as shown below

import Package2.InnerPackage.InnerModule as inmd

inmd.innerfunc1()


## Is it possible to get it done without typing entire path ???

'''

## Above stated problem can be solved by adding --- from Package2.InnerPackage.InnerModule import *
## in the __init__.py file of Package2

import sys

'''
import Package2

Package2.innerfunc1()  ## Now we can directly access innerfunc1() 

print(sys.modules.keys()) ## 'Package2', 'Package2.InnerPackage', 'Package2.InnerPackage.InnerModule' ... will be keys
print(globals().keys()) ## 'Package2' will be key

'''

