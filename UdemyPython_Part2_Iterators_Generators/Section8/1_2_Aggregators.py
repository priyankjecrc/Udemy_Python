def Squares(n):
    for i in range(n):
        yield i**2

sq3 = Squares(3)

print(next(sq3)) ## 0
print(next(sq3)) ## 1
print(next(sq3)) ## 4
## print(next(sq3)) ## StopIteration

## print(min(sq3)) ## ValueError: min() arg is an empty sequence... because sq3 has been exhausted


sq4 = Squares(4)
print(min(sq4)) ## 0
## print(min(sq4)) ## ValueError: min() arg is an empty sequence... because sq4 has been exhausted

## Now see strange behaviour

print(bool(sq4)) ## True... Why ??  - we have seen above that it has been exhausted but still it returns true
print((sq4))     ## This is because Generators does not implement __bool__ and __len__. If neither is present True is returned.Check 1_1 Aggregators


## Few Good Examples discussed in lecture

## Let's say, if we wish to check if all the elements of list are number

from numbers import Number

l = [10,20,30,40]

## Method1 -- less Pythonic way

def is_numeric(num):
    return isinstance(num, Number)

pred_l1 = map(is_numeric, l)
print(list(pred_l1))  ## [True, True, True, True]

## Method2

pred_l2 = (is_numeric(num) for num in l)
print(list(pred_l2))  ## [True, True, True, True]

## Method3

pred_l3 = map(lambda x: isinstance(x,Number),l)
print(list(pred_l3))  ## [True, True, True, True]

print(all(pred_l1)) ## True
print(all(pred_l2)) ## True
print(all(pred_l3)) ## True
