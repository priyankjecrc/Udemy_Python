### First Read from - https://realpython.com/python-dicts/
### Then read from  - VV Imp Read from - https://realpython.com/python-hash-table/#understand-the-hash-function

### Python does not have built-in support for Arrays
### List = array of pointers in python

## If we define __eq__ in class than python takes hash away.
## Hash in python basically involves id ie memmory location.
## In dictionary we say that keys must be immutable but correct way is to say that keys must be hashable.
## For a class to be Hashable it should implement both __hash__ and __eg__ methods
## We can use mutable objects as keys if we implement Hash function in them
## Remember Hash and Equal contract... If 2 objects are equal then their Hash values must be same...Same thing doesn't goes with vise versa
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


## Dictionaries can't be ordered because keys could be anything.
## In the following example there is no way we can sort keys..because one key is -> 100 and another is 'Two'


mydict = {100:'Hundred',
          'Two': 2}

print(mydict[100])  ## Hundred
print(mydict['Two'])## 2


