
## The garbage collector destroys objects that are no longer referenced
## The __del__ method will get called right before the object is destroyed by Garbage Collector hence GC will decide when to call __del__ method

## When we call __del__ method, we are only removing reference to the object. The GC will determine when to call the __del__ method
## We can't control __del__ method. It usualy gets called by GC when all the references to the object are gone

## Additional issues
## if __del__ contains reference to global variables, or other objects
## -> those objects might be gone when __del__ is called

## IF an exception occurs in __del__ method, it will not be raised by Python. It is silenced
## Prefer using context managers if you want to clean up the resources


import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value



class Person():
    def __init__(self,name):
        print('inside init')
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'

    def __del__(self):
        print(f'__del__ called for {self}...')



p = Person('Alex') ## Apart from O/p - anything we also egts O/P - __del__ called for Person(Alex)...
                   ## Because programs gets terminated automatically and __del__ gets called at the very end,
                   ## however we shouldn't bother so much about this

p_id = id(p)
print(ref_count(p_id)) ## 1.. showing that only one reference is associated (p itself) with the location p is pointing to

print('before None')
## p = None     ## This will call __del__ method
## del(p) ## This will call __del__ method

## Try something weird

p1 = p

del(p) ## __del__ will not be called, however reference p will be dropped but object is still referenced by p1
del(p1) ## __del__ will be called because now both reference(p and p1) are gone and object can safely be deleted by GC
        ## but still we can't tell when __del__ is going to run




























