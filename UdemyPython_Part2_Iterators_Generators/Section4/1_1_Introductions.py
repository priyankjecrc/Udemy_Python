## Video 32 - 37 has been covered below

## Iterators follows Lazy Evaluation
## Iterators are consumable - once they are finished, we can't use them again
## Iterables - these are those which implement Iterators

## Iteration doesn't always means indexing... sets are iterable but can't be indexed


class Squares():
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if (self.i > self.length):
            raise StopIteration

        else:
            result = self.i**2
            self.i += 1
            return result



sq1 = Squares(3)

print(sq1.__next__())  ## 0
print(sq1.__next__())  ## 1
print(sq1.__next__())  ## 4
print(sq1.__next__())  ## 9
## print(sq1.__next__())  ## Exception: StopIteration ...


sq2 = Squares(3)

print(next(sq2))  ## 0
print(next(sq2))  ## 1
print(next(sq2))  ## 4
print(next(sq2))  ## 9
## print(next(sq2))  ## Exception: StopIteration

## On the above class we can't do FOR loop, although we can do WHILE loop


sq3 = Squares(3)

while True:
    try:
        print(next(sq3))
    except StopIteration:
        break

## 0
## 1
## 4
## 9


## Can we do something so that we can use FOR loop ?? ... It can be done by adding __iter__()


class SquaresAgain():
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __iter__(self):
        return self


    def __len__(self):
        return self.length

    def __next__(self):
        if (self.i > self.length):
            raise StopIteration

        else:
            result = self.i**2
            self.i += 1
            return result

sqa1 = SquaresAgain(3)      ## sqa1 is an ITERATOR as __iterator__() has been implemented


for i in sqa1:               ## Now I can use FOR loop... I can also use enumerate
    print(i)                 ## Important point here to note is  -

                             ## 1. __iter__ gets called FIRST and will be called only ONCE and FIRST time
                             ## 2. __next__ will be called on the RETURNED value of __iter__, and will be called multiple times ... It can be confirmed by using Debugger
## 0
## 1
## 4
## 9


for k in sqa1:   ## This will not work as iterator has been exhausted
    print(k)


## Problem... we can't start iterator(sqa1) once it has been exhausted.. We will have to create new object for that
## Can we do something so that we dont have create new object everytime of the class --- It can be done by separating the class from iterator
## Although in this process we will have to create iterator object again and again once it is exhausted, but at least we don't have to create class
## object again