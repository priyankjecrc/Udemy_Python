import collections
class Human():
    pass


class Person():
    pass

h1 = Human()
p1 = Person()

print(p1 == h1)



print(isinstance(id(h1), collections.Hashable))