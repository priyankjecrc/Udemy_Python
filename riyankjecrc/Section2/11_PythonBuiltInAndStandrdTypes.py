
## Few types are builtin for eg - int, string, list, tuple
## Few types are not builtin eg - functions, modules, generators. These types are not part of builtin but they are part of another module
## for eg - function is present in Types module

import types



class MyClass():

    def doNothing(self):
        print('doing nothing')

print(type(MyClass.doNothing))
print(isinstance(MyClass.doNothing,types.FunctionType))   ### True...Make note of types.FunctionType
                                                          ### MyClass.doNothing is actually a function which belong to types.FunctionType
                                                          ### types in a module

obj = MyClass()
print(type(obj.doNothing))
print(isinstance(obj.doNothing, types.MethodType))        ### True ... Make note of types.MethodType