## Good to understand it from video no 86

## groupby(iterable,key_func)

from itertools import groupby

l = [(1,10,100),(1,11,101),(1,12,102),(2,20,200),(2,21,201),(3,30,300),(3,31,301),(3,20,302)]

groupedData1 = groupby(l,lambda x:x[0])  ##   groupedData1 will be like -         1,  subiterator
                                         ##                                       2,  subiterator
                                         ##                                       3,  subiterator
##print(list(groupedData1))

## [
#   (1, <itertools._grouper object at 0x000001CDA6408648>),
#   (2, <itertools._grouper object at 0x000001CDA6408688>),
#   (3, <itertools._grouper object at 0x000001CDA64086C8>)
## ]


print(next(groupedData1)) ## (1, <itertools._grouper object at 0x000002AAF6778608>) ... its a tuple... value of <itertools._grouper object at 0x000002A677F39CC8> - (1,10,100),(1,11,101),(1,12,102)
print(next(groupedData1)) ## (2, <itertools._grouper object at 0x000002AAF6778608>)
print(next(groupedData1)) ## (3, <itertools._grouper object at 0x000002AAF6778608>)



groupedData2 = groupby(l,lambda x:x[0])

element_1 = next(groupedData2)
print(element_1[0],list(element_1[1]))  ## 1 [(1, 10, 100), (1, 11, 101), (1, 12, 102)]

element_2 = next(groupedData2)
element2Val = element_2[1]

print(next(element2Val)) ## (2, 20, 200)
print(next(element2Val)) ## (2, 21, 201)
## print(next(element2Val)) ## StopIteration-





