
## Exceptions are not necessarily Errors. They dont necessarily result in program termination
## Exceptions are objects. They are instances of some class
## When an exception is raised, a propagation gets triggered. Now we can intercept this propagation and can raise an exception. This is
## called as exception handling. If exception doesn't gets handled it will propagated upto the caller. Call stack trace is maintained in this process
## Call Stack - Origin of the call is at the bottom. Latest call is at top of stack


## 2 Main categories of Exception - 1) Compilation Exception (eg: Syntax Error)
##                                  2) Execution Exception (eg: Value Error, Key Error, StopIteration)

## Look into Exception Hierarchy diagram

## IMP:

## BaseException:
     ## 1. SystemExit
     ## 2. KeyboardInterrupt
     ## 3. Generator Exit
     ## 4. Exception: Every other exception type in python is grouped under this
                    ## Therefore when we create custom Exception we will inherit from Exception Class and not from BaseException class

## If we catch an "Exception" exception, it will also catch any "Subclass" of Exception



def temp():   ## How i can be accessed , as it was declared later - https://www.youtube.com/watch?v=K7PJ89-MPOo
    print(i)

i = 3

temp()

