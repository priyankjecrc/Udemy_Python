### Read from - https://realpython.com/python-dicts/

## If we define __eq__ in class than python takes hash away.
## Hash in python basically involves id ie memmory location.
## In dictionary we say that keys must be immutable but correct way is to say that keys must be hashable.
## For a class to be Hashable it should implement both __hash__ and __eg__ methods
## We can use mutable objects as keys if we implement Hash function in them
## Remember Hash and Equal contract
## Watch video Python 3: Deep Dive video no 54 Hashing and Equality - Coding


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

obj1 = Person('pinkoo')
obj2 = Person('pinkoo')

print(hash(obj1),hash(obj2))
print('pinkoo'== 'pinkoo')
print(obj1 == obj2)


