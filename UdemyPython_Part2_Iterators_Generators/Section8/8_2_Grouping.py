## Some Caveats

## Caveat 1

from itertools import groupby

l = [1,1,1,2,2,2,3,2,2]

groupl = groupby(l) ## when we don't specify the key function, than it uses the data itself

print(list(groupl))

## [
# (1, <itertools._grouper object at 0x0000014B58572DC8>), --- 1, [1, 1, 1]
# (2, <itertools._grouper object at 0x0000014B58431C48>), --- 2, [2, 2, 2]
# (3, <itertools._grouper object at 0x0000014B5844B1C8>), ----3, [3]
# (2, <itertools._grouper object at 0x0000014B58469CC8>)  ----2, [2,2] .... This should not be happening.. therefore it's always better to sort the data
# ]


## ===========================================================================================================================================



## Caveat 2 .. next(groups)..(in below example we are doing next(groupedData) ) .. so next(groups) actually iterates through all elements of the
               ## previous subiterator... Video no 27 says current subiterator, but my analysis has shown previous subiterator

               ## It can be shown with below example

## Imp thing to notice is - The sequence of elements produced by 'SUBITERATOR' are all produced from 'same' underlying iterator
## Here it means that, as shown below, all the elements produced by 'SUBITERATOR' will be produced by 'iterdata'

## Means for eg - in this - (1, <itertools._grouper object at 0x000002AAF6778608>)
## when next is applied on <itertools._grouper object at 0x000002AAF6778608>, than elements will be produced from 'iterdata'



data = [(1,10,100),(1,11,101),(1,12,102),(2,20,200),(2,21,201),(3,30,300),(3,31,301),(3,20,302)]

iterdata = iter(data) ## making data as iterator...
                      ## We have made data as iterator because data is actually list and list is iterable hence how much of list is consumed can't be shown

groupedData = groupby(iterdata,lambda x:x[0])

key1,group1 = next(groupedData)


print(key1)              ## 1

## print(list(iterdata)) ## commented because list(iterdata) will consume iterdata
                         ## [(1, 11, 101), (1, 12, 102), (2, 20, 200), (2, 21, 201), (3, 30, 300), (3, 31, 301), (3, 20, 302)]
                         ## above does not include (1,10,100)...  why ?
                         ## Because as of now we it doesn't need to reach group2, therefore (1, 11, 101), (1, 12, 102) hasn't been iterated
                         ## After iterating (1, 11, 101), (1, 12, 102), group2 will come

key2, group2 =  next(groupedData)

print(key2)             ## 2
print(list(iterdata))   ## [(2, 21, 201), (3, 30, 300), (3, 31, 301), (3, 20, 302)]
                        ## above does not include - (1,10,100),(1,11,101),(1,12,102) ... but why??
                        ## Because in order to reach to next group it has to iterate, therefore (1,10,100),(1,11,101),(1,12,102) got iterated
                        ## Here because there is need to reach group2, hence (1,10,100),(1,11,101),(1,12,102) got iterated






