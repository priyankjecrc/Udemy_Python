## Every Scope has NameSpace

## Global Scope is essentially Module Scope, it spans a single File only
## There is no concept of Truly Global Scope(across all modules in entire app) in python. The only exception are some of the
## available built-in globally available objects eg - True, False, None, Print, dict.


## VV IMP.. There is need to understand the difference between SCOPE and NAMESPACE
## Every scope has Name Space and bindings are stored in it.

## Global Scope are nested inside BuiltIn Scope.
## These Global scope can have their own Name space

## Functions - Functions have their own scope
## IMP - Every time a Function is called a NEW scope is created. Variables defined inside the function are assigned to that scope

## Local Scope -> Global/Module Scope -> Built in scope(True, False, None, Print, dict stays in Built in scope)

## SCOPE vs NAMESPACE
## In reality, there are multiple NAMESPACES existing at any given time while a Python program is running,
## and which NAMESPACE you have access to is determined by the SCOPE you are currently in, ie the scope you are currently in determines which namespaces are available for you to use

## RULE - GLOBAL and LOCAL SCOPING
## When Python encounters a Function definition at COMPILE time, following rules are followed-

## 1. It will scan for any variables that have value assigned to them (eg a = 10). If the variable is specified as GLOBAL, then
##    it will be GLOBAL otherwise it will be LOCAL

## 2. Variables that are referenced but not assigned a value, will NOT be LOCAL and python at run time will look for them in ENCLOSING scopes



## IMP ----
def someFunc(a,b):  ## At COMPILE TIME, python determines that somefunc, a, b and c are going to be LOCAL variables.
    c = a*b         ## c is local variable. That is understandable because of RULE, but why a & b. Might be because while calling
    return c        ## someFunc, they will be assigned a value. Not sure about reason but a & b will be local for sure
                    ## Compiling doesn't create SCOPE or the NAMESPACE because we haven't called the function yet. But it predetermine at compilation time
                    ## that a,b and c, when they will be created and put into Namespaces it will be into Local Namespaces






def myFunc(b): ## Label -myFunc will be in Global Scope here
    a = 10   ## Variables defined inside a function are not created until the function is called (called means Run Time)
             ## Actually no Scope is created when a function is defined (means Compile time)
             ## Scope gets created when the function is called
             ## At compile time, python determines that a,b will be in  -> Local Name Space


# When Python encounters a Function definition at Compile time, it will scan for any labels(variables)
# that have values assigned to them. Those Labels will be considered as Local if they are not declared as Global

# Variables that are referenced but not assigned a value anywhere in the function will not be Local and python at run time, will look for them in enclosing space


someval = 100

def testFunc():
    global someval  ## We are telling that someval that we wish to refer is in Global scope
    print(someval)
    someval = 200
    print(someval)


testFunc()   ## 100
             ## 200

## Now after function testFunc() call, the LOCAL SCOPE and NAMESPACE will be destroyed


print(someval) ## 200

