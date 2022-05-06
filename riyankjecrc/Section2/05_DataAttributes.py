
class MyClass():
    language = 'python'   ### Data attribute -> language

obj = MyClass()

print(MyClass.__dict__) ## Namespace of class. This namespace contains attribute language
print(obj.__dict__)     ## Namespace of object. This namespace is empty

print(obj.language) ## If namespace of object is empty than how this will return 'python'
                    ## It first looks in the object namespace or in obj.__dict__. If it doesn't finds it there
                    ## it will look into MyClass namespace

### Imp

obj.language = 'Java' ### This will be called as instance attribute not class attribute
print(obj.__dict__) ## This will not be empty anymore. It will have language:Java in its name space
print(obj.language) ## therefore this will print Java
print(MyClass.language) ## This will still print 'python'

### Imp - Mark the difference below

print(type(MyClass.__dict__))  ## It is of MappingProxy type
print(type(obj.__dict__)) ## It is of dict type ie regular dictionary
                    ## We can't edit MappingProxy but we can edit dict ie it is mutable

obj.__dict__['version'] = 3.7 ## we have mutated dict of object

print(obj.__dict__)