
## Lambdas are not equivalent to Closures.. Many times we confused them with Closures. But they can be Closures


## Lambdas are just another way of creating functions
## Syntax:  lambda[parameter list]: expression.... parameter list is optional
##                                  expressions are evaluated and returned when lambda is called

## lambda[parameter list]: expression ---> We are not running this now hence it is not evaluating expression.. This whole will return a function object
## It is just like def.. It creates a function not run the function
## When we run or call lambda - lambda[parameter list]: expression... expression will be evaluated and returned

## lambda x: x**2  - will return x**2
## lambda : 'hello' - No parameters.. it will just return 'hello'

print(type(lambda x:x**2))  ## <class 'function'> .. we are not calling lambda here...it returns a function object
print(lambda x:x**2)   ## <function <lambda> at 0x000002088D81EB80>

myfunc = lambda x: x**2
print(myfunc(4))                ## 16 - This is actually calling lambda

def applyLambda(x, func):
    return func(x)

print(applyLambda(4, lambda x:x**2))  ## 16

## LIMITATIONS of Lambda

## 1. The body of lambda is limited to a single expression
## 2. IMP - No assignments:  lambda x: x = 5  - Not allowed
## 3. No Annotations