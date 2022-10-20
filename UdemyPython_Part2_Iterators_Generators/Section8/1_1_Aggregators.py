## What are Aggregators? - Function that iterate through an iterable and return a single value

## Associated Truth value : every object in python has an associated Boolean Value
## Every object in True except following
## 1. None
## 2. False
## 3. 0
## 4. Empty sequence type - eg - list, tuple, string.. if there is any element in them they will be True
## 5. Empty mapping types
## 6. Any custom class that has __bool__ or __len__ - Python will check __bool__ first, if its not there it will check __len__ function
                                                      ## if __bool__ says false then False, if __bool__ is not there and __len__ say 0, then also False
                                                      ## IMP - If nothing is present, __bool__ is not present and __len__ is not present than True will be returned


## Any and All functions

## any(iterable) - will return True if any element is Truthy, otherwise False
## all(iterable) - will return True if all elements are Truthy, otherwise False

## Predicate - Any function that takes Single argument and returns True or False is called as predicate
##             Predicate is used with Any and All functions

l = [1,2,3,4,100] ## we wish to check if all the elements are < 10

pred = lambda x:x<10

## How can we apply predicate
## 1. using Map function
## 2. Using List Expression or Generator Expression
## 3. There could be other ways
