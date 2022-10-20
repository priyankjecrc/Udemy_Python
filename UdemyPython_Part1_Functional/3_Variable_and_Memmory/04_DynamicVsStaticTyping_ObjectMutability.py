
## VV IMP -

name = 'Priyank'   ## here 'Priyank' is stored in heap and reference 'name' -> points to location where 'Priyank' is stored.
                   ## Hence while referring 'name' don't think of it as a variable. Always think of it as memmory location.
                   ## hence think of 'name' here as a memmory location


## Static typing - like in Java - String myvar = 'abc'... myvar = 10 will not work in java
## Dynamic Typing - myvar = 'abc' ..... myvar = 10 will work in python

## IMP....This is going to be useful to understand below
## Object has
## a) Type
## b) State

## Changing Data inside the Object is called modifying the Internal State

## It can be demonstrated with following example

class testClass():
    name = 'priyank'

obj1 = testClass()
print(hex(id(obj1)))   ## 0x2895f819488

obj1.name = 'pinkoo'
print(hex(id(obj1)))   ## 0x2895f819488 ... No change in obj1 address.. as Only the STATE of object is changed


a = 10
print(hex(id(a)))  ## 0x17480186a50

a = a+5
print(hex(id(a))) ## 0x17480186af0

## Strange Case

b = 10
c = 10

print(hex(id(b)), hex(id(c)))  ## 0x20395666a50 0x20395666a50 - same but why ?
                               ## Python automatically decides to reuse memmory references or it can create shared reference in case of immutable object
                               ## With mutable object , python will never create shared reference
                               ## IMP - but it will not do for every value, for eg c python has range of (-5 to 256) and any value in this range will be
                               ## considered for shared memmory (Video 25 Python Optmimizing and Interning @ 9.11). Its because small integers shows up
                               ## frequently in code, so better to have shared reference

## An object whose internal state can be changed is called as mutable - lists, sets, dictionary
## An object whose internal state can't be changed is called as immutable eg - int, float, boolean, strings, tuples, Frozen sets etc

## Good Case

a = [1,2] # Mutable
b = [3,4] # mutable

t = (a,b) # Tuples are immutable
print(t) # ([1, 2], [3, 4])

a.append(5)
b.append(6)

print(t) # ([1, 2, 5], [3, 4, 6]) - Tuples are immutable but the list it contains is mutable. Here in tuple, memory address of a and b is still same
                                    ## in a way from our perpective 't' changed

list1 = [1,2,3,4]
print(hex(id(list1)))  ## 0x296003c9040

list1.append(5)
print(hex(id(list1)))  ## 0x296003c9040 - Append modifies STATE(means we are modifying internal state of object) of list...
                       ## No change in memmory address after appending 5

list1 = list1+[6]      ## we are combining 2 list
print(hex(id(list1)))  ## 0x212461874c0 - This will not modify STATE of list... it will return a new object as we are combining 2 list


## Discussing Some interesting Cases

city1 = 'Pune'
city2 = city1  ## city1 and city2 points to same memory location

city1 = 'Mumbai'

print(city1) ## Mumbai
print(city2) ## Pune ... but why?, why not 'Mumbai'.. This is because string is immutable
             ## we pointed city1 to different memory location, but city2 is still pointing to same old memmory location


## Another interesting example

state = 'Maharashtra'

mylist = [1,2,3,state]  ## List is actually array of pointers...
                        ## therefore in place of 1,2,3   -> we have there memmory address
                        ## in place of state -> we have memmory address of location where 'Maharashtra' is stored

print(mylist)  ## [1, 2, 3, 'Maharashtra'] ... nothing surprising here

state = state+' India'  ## now state points to different memmory location

print(mylist) ## [1, 2, 3, 'Maharashtra'].... WOW... why still 'Maharashtra' ????...
              ## Just in previous line we change  'state' to 'Maharashtra India'.
              ## This is because we are thinking that mylist[3] is associated with 'state', but infact it is pointing to
              ## old memmory address which state was pointing to before modification. And at that old memmory location we still have 'Maharashtra'


