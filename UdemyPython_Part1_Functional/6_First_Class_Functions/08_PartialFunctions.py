
## We will start straight from examples
## A good example to sort distance of 2 coordinates using partial function - Video 93 after 19.00 mins

from functools import partial



def calSum(x,y):
    print(x+y)

## ---------------------------------------------------------------------------------------------------------------------------------------

partialSum = partial(calSum,10)

partialSum(20)  ## 30


partialSum = partial(calSum,y = 10)

partialSum(20)  ## 30


partialSum = partial(calSum,x = 10)

partialSum(y = 20)  ## 30

## ---------------------------------------------------------------------------------------------------------------------------------------

xval = 100      ## Imp Case

partialSum = partial(calSum,xval) ## Here x and xval are pointing to same memmory add. Actually it is not correct to say that x is pointing to
                                  ## same memmory add. It is correct to say that memmory address of 100 is baked into the partial
partialSum(y = 20) ## 120


xval = 500                     ## xval assigned to some other memmory address

partialSum(y = 20)  ## 120 .... Still  ## xval assigned to some other memmory address but x is still poinitng to same memmory add


## ---------------------------------------------------------------------------------------------------------------------------------------


def printList(x,y):
    print(x,y)

xList = [1,2,3,4]

partialList = partial(printList,x = xList)

partialList(y = 200) ## [1, 2, 3, 4]  200

xList.append(100)

partialList(y = 200)  ## [1, 2, 3, 4, 100]  200 ## Why ?
                      ## x and xList point to same memmory address. xList mutates list present at same memmory address, therefore
                      ## changes will also be seen in x


## ---------------------------------------------------------------------------------------------------------------------------------------

## Cases of confusion


def calSum(x,y):
    print(x+y)

sum = partial(calSum, y = 20)
sum(10, y = 200)   ## We have overridden y = 20 ... Try to avoid this