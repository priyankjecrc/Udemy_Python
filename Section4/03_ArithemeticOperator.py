
## Better watch video on Arithmetic Operators

## https://realpython.com/operator-function-overloading/

class Mock:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return self.num + other

    def __radd__(self, other):
        return self.num+other


mock = Mock(5)
mock = 5+mock
print(mock)

mock1 = Mock(10)
mock2 = Mock(10)
a = -2570
b = -2570


print(mock1 == mock2)