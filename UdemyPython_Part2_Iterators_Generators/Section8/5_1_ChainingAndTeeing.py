## Chaining doesn't look importatnt
## Will be discussing Teeing

## Why use Tee?
## Sometimes we need to iterate through ame ITERATOR(not iterable) multiple times. For this we can use Tee function

from itertools import tee

l = [1,2,3]

teelist = tee(l,5)

print(list(teelist)) ## [<itertools._tee object at 0x00000245B9BD9148>, <itertools._tee object at 0x00000245B9D26788>, <itertools._tee object at 0x00000245B9E53D48>, <itertools._tee object at 0x00000245B9D11BC8>, <itertools._tee object at 0x00000245B9D2B148>]

print(list(teelist[0])) ## [1, 2, 3]
print(list(teelist[1])) ## [1, 2, 3]

## Imp - important thing to notice that each copy of [1,2,3] is different object and they will have different memory location