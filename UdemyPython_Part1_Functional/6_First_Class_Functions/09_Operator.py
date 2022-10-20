## Video no 94 - have not watched video after 9 mins

## Look at following link for all the operators
## https://docs.python.org/3/library/operator.html

## Arithmetic Functions few eg -

## 1. add(a,b)
## 2. mul(a,b)
## 3. pow(a,b)
## 4. mod(a,b)
## 5. floordiv(a,b)
## 6. neg(a)

import operator
from functools import reduce

print(dir(operator))

l1 = [1,2,3,4]

print(reduce(operator.add,l1)) ## 10


## Comparison and Boolean Operator few eg -

## 1. lt(a,b)
## 2. le(a,b)
## 3. gt(a,b)
## 4. ge(a,b)
## 5. eq(a,b)
## 6. ne(a)
## 7. is_(a,b)   "Same as a is b."
## 8. is_not(a,b)  "Same as a is not b."


## Sequence and Mapping operators few eg -

## 1. concat(s1,s2)
## 2. contains(s,val)
## 3. countOf(s,val)
## 4. getitem(s,i)
## 5. setitem(s,i,val)  ## Works when s is mutable
## 6. delitem(s,i) ## Works when s is mutable

## itemgetter function

l1 = [1,2,3,4,5]

f  = operator.itemgetter(1,3,4) ## kind of partial function
print(f(l1))  ## (2, 4, 5)


