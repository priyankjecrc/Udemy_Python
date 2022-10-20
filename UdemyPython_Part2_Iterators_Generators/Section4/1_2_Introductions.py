
## Proving that __next__ will be called on the RETURNED value of __iter__ as mentioned in 1_1_Introductions


class Half():
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
            result = (self.i)/2
            self.i += 1
            return result


halfobj = Half(6)


class Squares():
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __iter__(self):
        return halfobj    ## Returning object of class Half


    def __len__(self):
        return self.length

    def __next__(self):
        if (self.i > self.length):
            raise StopIteration

        else:
            result = self.i**2
            self.i += 1
            return result

squareObj = Squares(3)

for i in squareObj:
    print(i)

## 0.0    O/P - shows that __next__ was called on the return value of __iter__
## 0.5
## 1.0
## 1.5
## 2.0
## 2.5
## 3.0