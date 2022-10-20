
## These are also called as Accumulators, Aggregators or Folding function
## Few examples : They are also builtin reducing functions
# Min,
# Max,
# Sum,
# Any,  - True, if any element is True
# All,  - True if all elments are True

## Explaining working with example. Lets say we want to find sum of element in list

l1  = [5,2,6,6,5,4,3,3,2,4,6]

sum = 0
for num in l1:
    sum = sum+num

print(sum)

## Reducer works in kind of similar fashion.. First it will take - 5,2 and result will be stores in resultVar.
## now resultVar, 6 will be used and result will be stores in resultVar..

## reduce - reduce(function, sequence, initial=_initial_missing):  --- We will discuss 'initial' later here
## function can be lambda or any other function. In the end, I have shown how to do without Lambda

from functools import reduce

l1  = [5,2,6,6,5,4,3,3,2,4,6]

print(reduce(lambda x,y:x+y, l1)) ## 46


## To calculate multiple

print(reduce(lambda x,y: x*y,l1)) ## 3110400

## To find Max

print(reduce(lambda x,y: x if x>y else y, l1)) ## 6

print(reduce(lambda x,y:max(x,y), l1)) ## 6 ... Anoither way

## To find Factorial of number = 6

print(reduce(lambda x,y: x*y, range(1,7))) ## 720


### Use of Initial

# reduce - reduce(function, sequence, initial=_initial_missing):  --- We will discuss 'initial' here

## If we want to find sum of all elements in a list, but what if list is empty
## When we give some value to initial, reduce starts from that value. If we dont give Initial it will default to None

l2 = []

print(reduce(lambda x,y:x+y,l2,0)) ## 0

## But Side effects of using initial

l3 = [4,5,6,7]

print(reduce(lambda x,y:x+y,l3,10)) ## 32... but it should be 22... It happened because it will consider first element as 10
                                    ## or in other words list will become [10,4,5,6,7]


## Reduce without Lambdas

def addFunc(x, y):   ## The function must be of 2 arguments
    return x + y

l4 = [2, 4, 7, 3]

print(reduce(addFunc, l4))  ## 16



