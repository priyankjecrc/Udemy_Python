
## VV IMP - Mark the difference between ITERATOR and ITERABLE
## ITERATOR can only be iterated once, after that it will be exhausted

## MAP
## Filter
## Zip
## List Comprehensions

## High order Function - A function that takes a Function as a parameter and returns Function as its return value

## MAP : High Order Function
## map(func, *iterables) -> No of Arguments that must be present in func == total no of iterables... Confusing..see below
## map(func, *iterables) - It returns an ITERATOR not Iterable

def myfunc(x):    ## As we will be using just one iterable which is l1, therefore no of arguments present in myfunc will be = 1 ie x
    return x**2

l1 = [1,2,3,4]    ## myfunc takes only one iterable as input, which is l1 here... l1 will be one iterable
                  ## if the definition of myfunc is like myfunc(x,y).. then it would have taken 2 iterables as input..

print(map(myfunc,l1))  ## <map object at 0x00000140153007F0>. We will have to add list or something else. As map returns a ITERATOR
                       ## that's why we have to add list or something else

print(list(map(myfunc,l1))) ## [1, 4, 9, 16]


def addLlist(x1,x2):
    return x1+x2

l1 = [1,2,3,4]
l2 = [10,20,30,40,50,60,70]

print(list(map(addLlist,l1,l2))) ## [11, 22, 33, 44] - since l1 is shorter, therefore will work as per no of elements in l1

## What will happen if No of Arguments that must be present in func < total no of iterables

l3 = [1,2,3,4,5,6,7]

result = map(lambda x,y:x+y,l1,l2,l3)   ## IMP ...
print(result)                           ## <map object at 0x000001FAA0D26550> .... No error, because it doesn't make calculation right away. It defers
                                        ## that until you request items from iterable (Lazy evaluation).

## print(list(result)) ## TypeError: <lambda>() takes 2 positional arguments but 3 were given







## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


## FILTER : High Order Function
## filter(func,iterable) - it just take single iterable. Filter returns ITERATOR not Iterable
## Will return an iterator that contains all the elements of iterable for which function call returns True

def filterVal(x):
    if x<3:
        return False
    else:
        return True

l3 = [1,2,3,4,5,6,7]

filterOP = filter(filterVal,l3)
print(filterOP)                   ## <filter object at 0x000002B1EB5C6908>
print(list(filterOP))             ## [3, 4, 5, 6, 7]



## Filter with No function

                                                      ## IMP .. 0 is not printed
print(list(filter(None,[0,100,200,300,400,500,600]))) ## [100, 200, 300, 400, 500, 600].... 0 is not printed..because 0 is considered as false




## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## ZIP : Not a High Order Function
## zip(*iterables). It will stop at the shortest iterator

l1 = [1,2,3,4]
l2 = [10,20,30,40,50,60,70]
l3 = [1,2,3,4,5,6,7]


print(list(zip(l1,l2,l3))) ## [(1, 10, 1), (2, 20, 2), (3, 30, 3), (4, 40, 4)] .. Stopped at shortest iterable l1 because it got exhausted first



## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



## LIST COMPREHENSION : Alternative to MAP and FILTER

def myfunc(x):    ## Instead of doing something like this, we can do the following
    return x**2

l1 = [1,2,3,4]

print([x**2 for x in l1]) ## [1, 4, 9, 16]

l1 = [1,2,3,4]
l2 = [10,20,30,40,50,60,70]

print([x1+x2 for x1,x2 in zip(l1,l2)])  ## [11, 22, 33, 44]


## another example of List Comprehension

def filterVal(x):      ## Instead of doing something like this, we can do the following
    if x<3:
        return False
    else:
        return True

l3 = [1,2,3,4,5,6,7]

print([x for x in l3 if x>3]) ## [4, 5, 6, 7]


## Combiming filter and map

print(list(filter(lambda y:y>25, list(map(lambda x:x**2, l3))))) ## But this can be done by List Comprehension easily. Check below

print([x**2 for x in l3 if x**2>25]) ## [36, 49]

## Above mentioned way will do all the calculation, but map() will not do all the calculation unless required

