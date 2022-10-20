## Different approach has been discussed in Video 40 cyclic iterators

mylist = [1,2,3,4,5,6,7,8,9,10]
direction = ['N','S','E','W']

## We wish to do something like -
'''
    1 N
    2 S
    3 E
    4 W
    5 N
    6 S
    7 E
    8 W
    9 N
    10 S
'''

lenDir = len(direction)

for indexval,i in enumerate(mylist):
    index = indexval % lenDir
    print(i, direction[index])


print([[i,direction[indexval % lenDir]] for indexval,i in enumerate(mylist)])



