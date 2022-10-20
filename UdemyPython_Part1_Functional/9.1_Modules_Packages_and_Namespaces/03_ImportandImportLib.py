
## lets say we have following situation

mod_name = 'math' ## math is a module which we want to import, but we wish to import this using 'mod_name'
                  ## we want to import using mod_name, but import mod_name will not work


## import mod_name ... This will not work

import importlib

importlib.import_module(mod_name) ## or importlib.import_module('math')
                                  ## This is how we can import


## There are 3 things
# 1. Finders: They are basically functions that looks for module which we wish to impoer
# 2. Loaders:
# 3. Finders+Loaders = Importers (They can both be  Finder and Loader)

