
## Decorators explained below

'''
outerFunc(passFunc):                 ## IMP... Here outerFunc is a decorator. It returns a Closure usually because innerFunc will be doing something with passFunc

    innerFunc(*args, **kwargs):
         "do something which is not done by passFunc"
         return passFunc(*args, **kwargs)

    return innerFunc                 ## 'Without Parameters'


let addNum be some function

addNum = outerFunc(addNum)  ## This is the purpose of decorators.  ------------ 1

@outerFunc
def addNum(a,b)
     return a+b   ## Here addNum will be passed to outerFunc and returned function will be assigned to addNum
                  ## as shown in ---- 1

'''

## Issue with this is that we actually loose all information about addNum, but there is solution to this problem

from functools import wraps  ## We will use Wraps which is again a decorator to deal with above issue


def counter(fn):
    count = 0
    @wraps(fn)                   ## This way we handle above issue. wraps are also decorator but watch how are we using wraps
                                 ## here... Instead of just @wraps we are using @wraps(fn), ie with parameters
    def inner(*args, **kwargs):
        nonlocal count
        count = count+1
        print(f'No of times function called  = {count}')
        return fn(*args, **kwargs)
    return inner


@counter
def addVal(a,b):
    ''' return sum of 2 numbers '''
    return a+b

help(addVal)  ## O/P - Help on function addVal in module __main__:
              ## addVal(a, b)
              ## return sum of 2 numbers


print(addVal(2,3)) ## No of times function called  = 1
                   ## 5



