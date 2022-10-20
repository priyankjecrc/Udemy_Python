
import math

print(type(math)) ## o/p -> module. And module is just a class. So math is instance of module
print(type(type(math)))

### Where to find this module class. It is actually in another module called as types (not type)

import types
print(dir(types))  ## here we can find module type

print(types.ModuleType is (type(math))) ## True... because type(math) will give module which is same as ModuleType

class Person:
    pass

p1 = Person()

print(id(Person.__eq__))  ## both will return same id
print(id(object.__eq__))
print(id(p1.__eq__))      ## Here different id will be returned from above two


