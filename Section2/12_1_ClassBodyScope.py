
## Module is actually name of file with extension .py. Here module is 12_1_ClassBodyScope.py
## Module has its own global space - It contains Python (the class we have defined) and p (the object)

class Python():  ## The class body has its own scope. It contains kingdom,phylum,family,__init__,say_hello

    kingdom = 'Animalia'
    phylum = 'chordata'
    family = 'pythonidae'

    def __init__(self, species):  ## __init__ is just a pointer to a function. __init__ as it's just a pointer it's scope is class body
        self.species = species    ## But the function that __init__ points to is nested in the scope which contains the class
                                  ## and that scope here is module 12_ClassBodyScope not class body scope

    def say_hello(self):       ## say_hello() is a pointer to a function. say_hello as it's just a pointer it's scope is class body
        return 'hello'         ## But the function that say_hello points to is nested in the scope which contains the class
                               ## and that scope here is module 12_ClassBodyScope not  class body scope

## Imp point - As the function is nested in scope of module therefore when python looks for a symbol in a function,
## it will not use the class body scope.
## If I use print(kingdom) inside say_hello(), it will not work


p = Python('monty')