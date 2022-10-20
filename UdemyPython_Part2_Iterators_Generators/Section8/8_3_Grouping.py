from itertools import groupby

data = [(1,10,100),(1,10,101),(1,12,102),(2,20,200),(2,20,201),(3,30,300),(3,31,301),(3,31,302)]

groupedData = groupby(data, lambda x: (x[0],x[1]))

## print(list(groupedData))

## [
#    ((1, 10), <itertools._grouper object at 0x00000233063A9D48>),
#    ((1, 12), <itertools._grouper object at 0x00000233063A9BC8>),
#    ((2, 20), <itertools._grouper object at 0x00000233063A9CC8>),
#    ((3, 30), <itertools._grouper object at 0x00000233063A9B88>),
#    ((3, 31), <itertools._grouper object at 0x00000233063A9C48>)
## ]

for key, value in groupedData:
    print(f'key = {key}, value =  {list(value)}')

## key = (1, 10), value =  [(1, 10, 100), (1, 10, 101)]
## key = (1, 12), value =  [(1, 12, 102)]
## key = (2, 20), value =  [(2, 20, 200), (2, 20, 201)]
## key = (3, 30), value =  [(3, 30, 300)]
## key = (3, 31), value =  [(3, 31, 301), (3, 31, 302)]