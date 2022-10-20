
## Watch video - Section 8 descriptors video no - 92 - Using as instance properties


class OneDigitNumericValue():
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:               ### Self - The discriptor object
        print(f' self = {self}, obj = {obj}, type = {type}')   ### obj  - The object __get__ was called from
        try:                                                   ### type - obj owner class
            return self.value[obj]
        except:
            return 0

    def __set__(self, obj, value) -> None:
        print(f' self = {self}, obj = {obj}, value = {value}')
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value



class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()              ## IMP - Any instance of Foo will point to same instance of Discriptor OneDigitNumericValue
my_second_foo_object = Foo()       ## its obivious because both the instance(my_foo_object, my_second_foo_object) will share number and
                                   ## number points to one instance of Discriptor OneDigitNumericValue
my_foo_object.number


print(my_foo_object.values)