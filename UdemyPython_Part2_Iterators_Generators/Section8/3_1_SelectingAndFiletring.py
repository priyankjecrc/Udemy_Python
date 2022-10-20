
## We will discuss about
## 1. filter - it's not a part of itertools
## 2. filterfalse
## 3. compress
## 4. takewhile
## 5. dropwhile
##    All returns an lazy iterator

from itertools import filterfalse, compress, takewhile, dropwhile

l = [1,10,2,11,3,12]

print(list(map(lambda x:x<4,l)))  ## [True, False, True, False, True, False]
print(list(filter(lambda x:x<4,l))) ## [1, 2, 3]
print(list(filterfalse(lambda x:x<4,l))) ## [10, 11, 12]



## VV IMP - Compress function
## It allows filtering of one iterable, using Truthiness of items in other iterable

data  = [1,2,3,5,10,11]
selectors = [True,True,False,False]

print(list(compress(data, selectors))) ## [1, 2] ... 10, 11 will be associated with None and None means False


## takewhile Function

l = [1,10,2,11,3,12]

print(list(takewhile(lambda x:x<4,l))) ## [1] ... takewhile will return an iterator with all the elements as long as it encounters 1st Truthy, moment it faces Falsy,
                                       ##         it will stop returning

## dropwhile Function

print(list(dropwhile(lambda x:x<4,l))) ## [10, 2, 11, 3, 12] ... dropwhile will return an iterator with all the elements which lies after the
                                       ##                        element that caused 1st Falsy
