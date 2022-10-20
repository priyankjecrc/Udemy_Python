### Retrieving attributes values from class - use getattr()

class MyClass:
    language = 'python'
    version = 3.6
    name = 'priyank'

print(getattr(MyClass,'language'))
print(MyClass.language) ### this is equivalent to getattr(MyClass,'language')

## print(MyClass.x) ## This will throw exception
print(getattr(MyClass,'x','not existing')) ## if attribute doesn't exist we can give some default value

### Setting attributes value using setattr() - This will mutate MyClass. It can also add attributes to the class after
### the class has already been created

### Python is Dynamic language. It means we can modify(add or delete something) classes after the class has been defined for eg - during runtime

setattr(MyClass,'language','java') ### We can also use MyClass.language = 'java'
print(MyClass.language)

### Imp - State of object is stored in a Dictionary
### MyClass is also an object

print(MyClass.__dict__) ## This will give us insight into the state of object, but not everything that makes state of object
                        ## is located in this dictionary. For eg -> __name__. It is not in this dictionary
                        ## __dict__ ->This will give us a Mapping Proxy Object which is actually not of dict type but it
                        ## is still a dictionary a HashMap. It is Read Only HashMap
                        ## We can't directly mutate Mapping Proxy for eg we can't set key values directly in Mapping Proxy
                        ## because it is Read Only, but setattr() can indirectly mutate MappingProxy

print(type(MyClass.__dict__))  ## <class 'mappingproxy'>


### We can delete Attributes at runtime by using deleteattr() or del for eg: - del MyClass.name

delattr(MyClass,'name')
print(MyClass.__dict__)

print(MyClass.__dict__['version'])  ## Not a good way to access values
                                    ## Just like dictionary we can pass key name( for eg 'version' here).
                                    ## But this might not work for everything as everything is not stored in Dictionary




