### Discussing few important things

### In the End some discussion on [] vs list ()

## VV IMP - Mark the difference between ITERATOR and ITERABLE
## ITERATOR can only be iterated once, after that it will be exhausted

mylist = [1,2,3,4]

def myfunc(x):
    return x**2

result = map(myfunc,mylist)   ## Will return an ITERATOR and not ITERABLE...
                              ## No actual calculations are performed at this point and just creation of map object

print(result)                 ## <map object at 0x0000021ECBEFE988>


for x in result:    ## Here we are requesting items and actual calculation will happen now
    print(x)        ## 1
                    ## 4
                    ## 9
                    ## 16

for y in result:
    print(x)      ## Will not print anything... Because result is ITERATOR and not ITERABLE.
                  ## ITERATOR can only be iterated once, after that it will be exhausted
                  ## that's why nothing was printed


## Solution to problem that ITERATOR can only be iterated once. Put iterator in list as show below

result1 = list(map(myfunc,mylist))

for x in result1:
    print(x)        ## 1
                    ## 4
                    ## 9
                    ## 16

for x in result1:
    print(x)        ## 1
                    ## 4
                    ## 9
                    ## 16


testDS1 = [1,2,3,4,5,6]
print(testDS1)          ## [1, 2, 3, 4, 5, 6]


### Lists can also be created with the built-in function list([iterable]).
## This function takes as argument an iterable (i.e. any type of sequence, collection, or iterator), returning a list with the items of the input object.

name = 'priyank'

namelist = list(name)
print(namelist)          ## ['p', 'r', 'i', 'y', 'a', 'n', 'k']