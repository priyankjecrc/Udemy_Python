
## We will see about - sys.exc_info()
## Here we will discuss about Bare Except
## When we use Bare Except, we cant use "as"
import sys

try:
    (1/0)
except:                                   ## We cant use 'as'. As we are not using 'as', how can we get handle to the exception ?
    print('Div by zero not allowed')      ## We can use sys.exc_info(). This returns 3 things
    print(sys.exc_info())                 ## O/P - (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001F09A4D7540>)
                                          ## 1. Exception Type, 2. Exception Value, 3. Exception Traceback (Which is call stack of Exception)