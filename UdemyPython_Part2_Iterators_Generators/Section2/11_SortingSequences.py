## Python Sorted Function

## sorted(iterable, key = None, reverse = False)

## Imp points -
## 1. sorted does not modify iterable, it makes copy of iterable and sort that.
## 2. After sorting a copy, it always return a List... even if iterable is a tuple or anything else.. it will always return a List
## 3. Sorting algorithm which is used in sorting is - TimSort
## 4. Stable Sort - It maintains the relative order of items that have equal keys
      ##   (p1,p2,p3,p4,p5)
      ##    10 20 5, 15 20 - P2 and P5 are same... When we sort based on values O/P will be - p3,p1,p4,p2,p5
      ##                                                                                      Stable Sort maintains order of p2 and p5


## Inplace Sorting - Means iterable will be sorted without creating copy
## List supports this In Place sorting. List has sort() method which will do inplace sorting, therefore mutating the list


tuple1 = (4,2,4,8,1,3,5,6)
print(sorted(tuple1))     ## [1, 2, 3, 4, 4, 5, 6, 8]....Natural sorting is done.... List is returned

set1 = {4,2,4,8,1,3,5,6}
print(sorted(set1))   ## [1, 2, 3, 4, 5, 6, 8]... Non sequence sorting..Again list is returned

dict1 = {3:100,2:200, 1:100}

print(list(dict1))  ## [3, 2, 1] ... list on dict will always return keys

print(sorted(dict1)) ## [1, 2, 3] ... will return sorted keys by default

dict2 = {1:100,2:200,'three':300}

## print(sorted(dict2))  ## TypeError: '<' not supported between instances of 'str' and 'int'




## Now what if I wish to sort dict based on values and not on keys

dict1 = {3:100,2:200, 1:100}

print(sorted(dict1, key = lambda k: dict1[k])) ## [3, 1, 2]



def retKey(passdict):
    return dict1[passdict]

print(sorted(dict1, key=retKey))  ## [3, 1, 2]


## Example of In Place Sort

mylist = [10,5,20,15,20,25]

print(sorted(mylist))  ## [5, 10, 15, 20, 20, 25]
print(mylist)   ## [10, 5, 20, 15, 20, 25] .... mylist is still same


mylist.sort() ## In place sorting
print(mylist)  ## [5, 10, 15, 20, 20, 25].... mylist mutated and sorted


## Sorting of some class

class MyClass():
    def __init__(self,name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'MyClass( {self.name}, {self.value} )'

    def __lt__(self, other):
        return self.value < other.value


c1 = MyClass('c1',20)
c2 = MyClass('c2',10)
c3 = MyClass('c3',15)
c4 = MyClass('c4',5)

classTuple = (c1,c2,c3,c4)

print(sorted(classTuple))  ## [MyClass( c4, 5 ), MyClass( c2, 10 ), MyClass( c3, 15 ), MyClass( c1, 20 )]



