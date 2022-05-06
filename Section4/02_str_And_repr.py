## __str__ and __repr__

## Both are used for creating string representation of object
## __repr__ is called when we call repr() on object
## __repr__ is used by developers to provide the information about the object itself for eg: we can give information on how the object was created


## __str__ is used by str() and print() and other formatting methods.
## Mostly used to display information to end user

## Imp - if __str__ is not implemented in your class than python will look for __repr__ instead
## If neiher __str__ not __repr__ is implemented and since all objects inherits from Object, will use __repr__ defined there instead

class MyClass():

    def __repr__(self):
        print('inside repr')

    def __str__(self):
        print('inside str')



## 1. __repr__ is called when only obj is typed

## 2. __str__ is called when print(obj) is typed

## 3. __repr__ can also be called using repr(obj), __str__ can also be called as str(obj)

## 4. by default __repr__ will give output like <__main__.Person object at 0x7f90024cb00>

## 5. when __str__ method does not exists python fall back to __repr__ method

## 6. when __repr__ is not present but __str__ is present then typing

   ## a) obj will print default repr value ie <__main__.Person object at 0x7f90024cb00>

   ## b) print(obj) will call __str__
