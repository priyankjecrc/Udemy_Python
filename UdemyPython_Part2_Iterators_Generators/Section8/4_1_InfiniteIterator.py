## We will discuss about

## 1. Count function
## 2. cycle function
## 3. repeat function

from itertools import count,cycle,repeat


## Count - Lazy iterator and is infinite. It is just like range function but with no limit

Countelements  = count(10,2)
print(next(Countelements))  ## 10
print(next(Countelements))  ## 12

## cycle - this function allows to loop over finite iterable indefinitely

l = ['a','b','c']

cycleElements = cycle(l)
print(next(cycleElements)) ## a
print(next(cycleElements)) ## b
print(next(cycleElements)) ## c
print(next(cycleElements)) ## a
print(next(cycleElements)) ## b

## repeat - this function yields same value multiple times.. because it repeats same object , there is need to be careful when we are repeating mutable objects

name = 'pinkoo'
repeatElements = repeat(name)    ## This will repeat name infinitely
repeatElements3 = repeat(name,3)
print(list(repeatElements3))     ## ['pinkoo', 'pinkoo', 'pinkoo']







