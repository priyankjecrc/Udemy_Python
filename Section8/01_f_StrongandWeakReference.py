
## Previous problem can be solved by storing weak reference to the object instead of storing object as key in Dictionary

## Weak Reference - Think of it as a reference to the object that does not affect the reference count as far as memmory manager is concerned
## Object will be garbage collected if there are no more strong references to the object.
## Weak reference will be considered dead if there are no more strong references

## Not every object in python supports Weak references and infact many of built in type donot support weak references

## Create Weak Reference
import ctypes
import weakref


class Person():
    pass

p1 = Person()
p2 = weakref.ref(p1)  ## weak reference created using strong reference p1


print(p1)  ## <__main__.Person object at 0x000001C79DF10FD0>
print(p2())  ## <__main__.Person object at 0x000001C79DF10FD0>. P2 is callable. It will return original object which is P1 in this case
            ## in ase P1 is already Garbage collected.. p2() will return None

print(p2)  ## <weakref at 0x000001C79DE6B180; to 'Person' at 0x000001C79DF10FD0> p2 is weak reference object. We can see weak ref object is
           ## pointing to Strong ref object


p3 = p2() ## Careful: as this will create another strong reference to p1


## Suppose we want to create Dictionary of weak references
## Actually weakref provides WeakKeyDictionary which is a dictionary but it holds weak references

weakDict = weakref.WeakKeyDictionary()

weakDict[p1] = 'some value' ## A weak reference will stored to the object p1 points to
                            ## if we do del p1. Strong reference will be gone and item will automatically be removed from weak key dictionary

### Imp - below is a function that tells how many references are there to an object

def ref_count(address):
    return ctypes.c_long.from_address(address).value  ## will only show Strong References. Weak reference even if exists will not be counted


print(ref_count(id(p1)))  ## 2 as there are 2 references to object pointed by p1

del p1
del p3
print(p2)  ## <weakref at 0x000001FE832F8B80; dead> -- With  all strong references are gone, we can see dead appearing in O/P


### Creating weak reference to List object. List object does not support Weak referecnes

l1 = [1,2,3]
## weakref.ref(l1)  ## TypeError: cannot create weak reference to 'list' object

p1 = Person()
p2 = weakref.ref(p1)

## Checking weak ref count

print(weakref.getweakrefcount(p1)) ## Check: We are not passing p2 in getweakrefcount. We are passing p1

print(p1.__weakref__) ## Where information about weak ref is stored?
                      ## It is stored in p1.

print(weakDict.keys())