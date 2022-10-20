
## Can we get reference count to an object


import ctypes
import sys

a = [1,2,3]
print(sys.getrefcount(a)) ## O/P = 2. This add one more reference by itself.
                          ## if I choose a = 10, it will give some unexplained value. Reason not known so far

print(ctypes.c_long.from_address(id(a)).value) ## O/P = 1. However id(a) will create one more reference but it releases that reference after returning memmory add value

b = a

print(ctypes.c_long.from_address(id(a)).value) ## O/P = 2

## Strange behaviour

c = [2,3,4]

c_id  = id(c)

print(ctypes.c_long.from_address(c_id).value) ## O/P = 1

c = None

print(ctypes.c_long.from_address(c_id).value) ## O/P = 0
print(ctypes.c_long.from_address(c_id).value) ## O/P = 0. It might some other value or any random value.. Because we have deleted reference to this
                                              ## memmory and now this memmory can be used for anything else bby python
