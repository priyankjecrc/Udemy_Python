
## Mapping - Applying a callable to each of the element

## Accumulation - Reducing an iterable down to single value

## Starmap - if we apply map to [[1,2],[3,4]], than map is applied to [1,2] as one argument and to [3,4] as other argument.
## Starmap on the other hand will take [1,2], will make them into 1,2 and then 1,2 will go as 2 arguments to function. Same thing will be done with [3,4]

from itertools import starmap, accumulate

l1 = [[1,2],[3,4]]

print(list(starmap(lambda x,y:x+y, l1))) ## [3, 7]

def squares(n):
    for i in range(n):
        yield i**2

class Squares():
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return squares(self.n)

sq3 = Squares(3)

print(max(sq3)) ## 4
print(min(sq3)) ## 0
print(sum(sq3)) ## 5



## Accumulate and Reduce functions... Reduce function comes from functools, accumulate comes from itertools
## They work more or less in same way
## https://codeburst.io/reduce-vs-accumulate-in-python-3ecee4ee8094 - for Accumulate vs Reduce

from functools import reduce

l = [1,2,3,4,5,6]

print(reduce(lambda x,y:x+y, l)) ## 21 ... Reduce will return Final result

accm = accumulate(l,lambda x,y:x+y) ## See here syntax is different than reduce
print(next(accm)) ## 1
print(next(accm)) ## 3
print(next(accm)) ## 6         ... Benefit of using Accumulate is that, I can get the intermediate results

