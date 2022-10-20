## Another example to demonstrte benefits of usinf property()

## Here to the outside world we are only showing age and internally we are saving value in _age
## When we do obj.   -> it will show age in options and not _age
## Variables declared with _ as prefix are not shown to outside world


class testClass():

    def __init__(self, pass_age, pass_name,pass_city):
        self.name = pass_name      ## obj. will SHOW 'name' in options
        self._age = pass_age       ## obj. will NOT SHOW '_age' in options. It will show just 'age' in options because of property()
        self._city = pass_city     ## obj. will NOT SHOW '_city' in options

    def __getAge(self):
        return self._age

    def __setAge(self, value):
        self._age = value

    age = property()
    age = age.getter(__getAge)
    age = age.setter(__setAge)



obj = testClass(50,'Adam', 'Atlantis')

print(obj.__dict__)  ## {'name': 'Adam', '_age': 50, '_city': 'Atlantis'}




