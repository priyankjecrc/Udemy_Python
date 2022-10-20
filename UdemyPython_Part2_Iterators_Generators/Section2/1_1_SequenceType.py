## Sequence types can be accessed by index..

## Set is iterable, but it can't be accessed by index. Therefore its not a sequence type


s = {1,2,3}
## print(s[0]) ## TypeError: 'set' object is not subscriptable


## IMP - Concatenation of Immutable vs Mutable... Be very careful
## We will be investigating '+' and '*'. Same thing happens in both cases

l1 = [1,2]               ## 1,2 are immutable
doublel1 = l1+l1
multl1 = l1*2
print(doublel1)     ##  [1, 2, 1, 2]
print(multl1)       ##  [1, 2, 1, 2]

print(id(l1[0]), id(doublel1[0]), id(doublel1[2]), id(multl1[0]), id(multl1[2]))  ## 140712832508320 140712832508320 140712832508320 140712832508320 140712832508320
                                                                                  ## All will share same memmory address

## Important to remember that '+' and '*' uses same memmory address
## Now this may create a problem in following situation


l2 = [[100,200]]   ## [100,200] is mutable

doublel2 = l2+l2
multl2 = l2*2
print(doublel2)   ## [[100, 200], [100, 200]]
print(multl2)     ## [[100, 200], [100, 200]]


## If I make changes in mutable object in l2 or doublel2 or multl2, in any of them... changes will be reflected in all....l2,doublel2,multl2
## because '+' and '*' uses same object... and if that object is mutable in nature and if I make changes in this mutable object... it will be
## reflected everywhere

l2[0][0] = 9000
print(doublel2)  ## [[9000, 200], [9000, 200]]
print(multl2)    ## [[9000, 200], [9000, 200]]

print([1,2,3].index(1))
