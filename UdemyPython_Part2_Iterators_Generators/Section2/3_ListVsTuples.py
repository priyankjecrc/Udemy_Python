
## Tuples are actually data structures.
## Tuples are more efficient than list. If we wish to use mutability we can go with List, otherwise its better to go with Tuples

## Tuples are immutable sequence types

## In lecture there is a discussion of Shallow vs Deep Copy - https://realpython.com/copying-python-objects/

## Better watch video 9 - Lists vs Tuple

## Some concept from the video

mylist = [1,2,3,4,5]
mytuple = (1,2,3,4,5)

mylistcopy = list(mylist)  ## will create a shallow copy
mytuplecopy = tuple(mytuple) ## will not create a shallow copy.. because it doesn't make sense to make a shallow copy of immutable sequence
                             ## because any change in immutable sequence will make new object. This is done by python because of optimization

print(id(mylist), id(mylistcopy))  ## 1756050575752 1756055088072  - Different address
print(id(mytuple), id(mytuplecopy)) ## 1756050676616 1756050676616 - Same Address