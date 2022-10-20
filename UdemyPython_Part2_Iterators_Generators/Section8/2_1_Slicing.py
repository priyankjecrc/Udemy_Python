
## We can slice Sequence types like this  - seq[i:j:k] OR seq[slice(i,j,k)]

## IMP - We can't use above method of slicing in case of ITERABLES, ITERATOR
## In case of ITERABLES, ITERATOR we will have to use islice(iterable, start, stop, step)

l = [10,20,30,40,50,60,70]

print(l[slice(1,5,1)]) ## [20, 30, 40, 50], 5th element won't be picked

from itertools import islice ## We can't use islice once exhausted

result = islice(l,1,5,1)
print(list(result)) ## [20, 30, 40, 50]
print(list(result)) ## []   because islice is exhausted