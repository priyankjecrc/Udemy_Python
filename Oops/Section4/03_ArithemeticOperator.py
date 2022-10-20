
## Better watch video on Arithmetic Operators

## https://realpython.com/operator-function-overloading/

class Mock:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __radd__(self, other):
        print(self)
        return self.num+other

    def __len__(self):
        return 100

mock = Mock(5)
mock = 5+mock
print(mock)

mock1 = Mock(10)
mock2 = Mock(10)
a = -2570
b = -2570


print(mock1 == mock2)
print(hash(Mock))
print(id(Mock))
print(dir(mock))
print(len(mock1))
print(bool(mock1))