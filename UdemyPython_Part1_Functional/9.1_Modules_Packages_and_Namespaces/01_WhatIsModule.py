
## Good to watch video - 136 Module and Recap
## Module is actually an object of a certain Data Type. Module is an instance of Module type, just like functions are instances of function type


a = 10

print(globals())  ## will have 'a': 10
print(locals())   ## ## will have 'a': 10 - locals and globals will be same here. Locals are generally used inside the function
print(locals() is globals())  ## True - shows that locals and globals are same here

def myFunc():
    a = 10
    b = 100
    print(locals())  ## it is the right place to use locals()

myFunc()     ## {'a': 10, 'b': 100}


### ===============================================  Reference has been taken from  video - 136 Module Recap  ==========================================================================

## Importing Module - For the first time (means that module was never imported before)

# 1. When you import the module, the entire module gets executed at runtime only


# 2. When for eg: import somemodule, get encountered, first python will look for 'somemodule' in paths contanied in sys.path

        # a. Finders will locate the module
        # b. If Finders were able to find module, than the code of module has to be loaded. Now Finders will return the ModuleSpec object
        #    This ModuleSpec will tell python that here is the loader that you need to use to load the module

# 3. If python is not able to find module in the paths contained in sys.paths, then wit will raise error and import will fail



# 4. If module is found in path present in sys.path, it is put into the memory first
#          a). An "EMPTY" module typed object is created and reference will be added to the system cache (sys.modules). And this happens before
#              the Module code is compiled and executed.(just remember all this happens to avoid circular references)

#          b). After COMPILING and EXECUTING Module code, reference is set in globals() (also called as module NAMESPACE or module.__dict__)



## =====================================================================================================================================



## Importing Module - For the Second time (means that module was imported before)

# 1. Python will check the sys.modules to see if there is an entry in the dict. If it finds entry in sys.modules, than it
#    will just use that reference and module will NOT BE imported again. and that's why module code is run just one time

# 2. IMP ---- one sys.module cache is maintained across all modules...
# 3. IMP ---- globals() will be different for different module, but one sys.module will be shared across all modules


## Since references also exists in globals(). it means if we delete entry from sys.modules, it will not be deleted from globals()
## therefore things will still work

# For eg  -

import TestModule  ## will print  This is TestModule. It also means that TestModule was executed just one time
import TestModule


import math  ## builtin

print(math.__spec__) ## ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')
print(math.__name__) ## math
print(math.__package__) ## ''

import fractions

print(fractions.__spec__) ## ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001D783F62648>, origin='C:\\Users\\japr01\\Anaconda3\\envs\\Cracks\\lib\\fractions.py')
print(fractions.__name__) ## fractions
print(fractions.__package__) ## ''
