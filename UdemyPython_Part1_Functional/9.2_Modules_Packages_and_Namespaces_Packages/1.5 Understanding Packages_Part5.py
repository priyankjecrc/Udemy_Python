
## Some more application of __all__ .... Purpose not achieved

## https://stackoverflow.com/questions/35727134/module-imports-and-init-py


## Referring to Package5

## Problem of Cyclic reference - also mentioned in 0.1 General Introduction.py under heading Case 1
## What I want here is that the desired functions must be available here so that I can run them as shown below
## For this I need all the functions in __init__ of Package5.
## For that I have used - from Package5.InnerPack import * in __init__ of Package5


## Problem Case : Only when I am executing code from within InnerPack, then following issue wil happen

## If I use import Package5.InnerPack.Module11 ( in __init__.py of InnerPack ie giving complete path in InnerPack), it will lead to cycle.
## Because we are already inside __init__.py of InnerPack.. When import Package5.InnerPack.Module11 is encountered it will see
## Package5 - so it will execute __init__ of Package5, then it will see InnerPack and will execute of __init__ of InnerPack and this will lead to cycle

## If we just give import Module11, it will cause problem when accessing package from outside because
## When importing a file, Python ONLY searches the directory that the entry-point script is running from and sys.path which includes locations such as the package installation directory



## What will happen if I execute code from here

## No cycle case as mentioned above will happen because

## 1. We are importing Package5 here and Inside __init__ of Package5 we are doing - from Package5.InnerPack import *
## Therefore first Package5 will be loaded in sys.modules when import Package5 ( as mentioned in below lines)
## When from Package5.InnerPack is encountered( in __init__ of Package5), then InnerPack will be loaded in sys.modules
## Now when control is in __init__ of InnerPack and this statement - from Package5.InnerPack.Module11 import * is encountered
## than InnerPack won't be loaded again because it is allready there in sys.modules. Hence __init__ of InnerPack won;t be run again therefore no cycle


import sys

import Package5

print('inside Package5')

print(sys.modules.keys())
print(globals().keys())

Package5.module11Func1()  ## This is module11 1st Function
Package5.module12Func1()  ## This is module12 1st Function
Package5.module13Func1()  ## This is module13 1st Function






