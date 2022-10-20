

## copy() is actually a 'shallow' copy
## copy() method is 'not' implemented in Immutable types. It doesn't make sense to make copy of immutable sequence
## in fact immutable sequence like tuple do not support copy() function

## Below is big caveat

mylist = [[1,2,3],4,6,7]
cp = []

for e in mylist:
    cp.append(e)

mylist[0][0] = 10
print(mylist)      ## [[10, 2, 3], 4, 6, 7]
print(cp)          ## [[10, 2, 3], 4, 6, 7]  -  Changes done is mylist are also reflected in cp.
                   ##                           This is because address of [1,2,3] is shared between mylist and cp
                   ##                           Therefore changes in [1,2,3] will be reflected in both



### copying in Mutable vs Immutable

list1 = [1,2,3]
tuple1 = (1,2,3)

list1_cpy = list(list1)
tuple1_cpy = tuple(tuple1)

print(id(list1),id(list1_cpy))     ## 1792102313416 1792103783112 - Diff memmory address
print(id(tuple1), id(tuple1_cpy))  ## 1792103796392 1792103796392 - same memmory address because it is immutable and due to optimzation
                                   ## python feels that is it unnecessary to make copies of Immutable

## Shallow Copy

'''
Shallow copy means 

1. First constructing a new collection object but its elements will point to same memory address as the elements of original sequence 

'''

## Method 1 .... Another method of shallow is also shown above with Heading --- Below is big caveat

# --------------------- List Case -------------------------

list2 = [[1,2,3],4,5]

list2_cpy = list(list2)

list2[0][0] = 100 ## We are not mutating list2... we are mutating [1,2,3] (which is a mutable list) in list2

print(list2)     ## [[100, 2, 3], 4, 5] ... Drawbacks of Shallow Copy
print(list2_cpy) ## [[100, 2, 3], 4, 5] ... Drawbacks of Shallow Copy

# ---------------------- Tuple Case ------------------------

tuple2 = ([1,2,3],4,5)
tuple2_cpy = tuple(tuple2)   ## tuple2 and tuple2_cpy will be same. ie no copy will be created

tuple2[0][0] = 100

print(tuple2)      ## ([100, 2, 3], 4, 5)
print(tuple2_cpy)  ## ([100, 2, 3], 4, 5)

print(id(tuple2), id(tuple2_cpy))  ## 1904367768744 1904367768744 .. Same memmory address


## Method 2

# --------------------- List Case -------------------------

list3 = [[1,2,3],4,5]
list3_cpy = list3.copy()  ## Will only make copy of list3 as whole.. Not the copy of individual elements present in list3

list3[0][0] = 100

print(list3)      ## [[100, 2, 3], 4, 5] ... Same thing as explained above in Method 1 List case
print(list3_cpy)  ## [[100, 2, 3], 4, 5] ... Same thing as explained above in Method 1 List case


# --------------------- Tuple Case -------------------------

tuple3 = ([1,2,3],4,5)
## tuple3_cpy = tuple3.copy()  ## AttributeError: 'tuple' object has no attribute 'copy'



## Deep Copy

'''

Deep copy means
 
1. First constructing a new collection object 
2. And then recursively populating it with copies of the child objects found in the original. 
   It is actually an iterative process in which we make copy of everything

'''

## Method 1 - Manually doing Deep copy

list4 = [[1,2,3],[4,5]]
list4_cpy = [e.copy() for e in list4] ## This will not work in [[1,2,3],4,5]... because 4.copy() and 5.copy() will not work
                                       ## This method will create problem for eg - if list4 = [[[1,2,3],4,5],[6,7]]
                                       ## because  [[1,2,3],4,5].copy() will just create copy of [[1,2,3],4,5] and not the copy of
                                       ## every individual element in it

list4[0][0] = 100

print(list4)       ## [[100, 2, 3], [4, 5]]
print(list4_cpy)   ## [[1, 2, 3], [4, 5]] ... changes done in list4 not getting reflected in list4_cpy


## Method 2 - Best way of implementing deep copy

from copy import deepcopy

list5 = [[[1,2,3],4,5],[6,7]] ### Same example that we mentioned in line no - 106...Method 1 of Deep copy above.
list5_cpy = deepcopy(list5)

list5[0][0][0] = 100

print(list5)      ### [[[100, 2, 3], 4, 5], [6, 7]]
print(list5_cpy)  ### [[[1, 2, 3], 4, 5], [6, 7]] .... Perfect


