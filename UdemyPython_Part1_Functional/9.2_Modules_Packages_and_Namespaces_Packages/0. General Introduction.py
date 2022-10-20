## Packages are Module, but not all modules are Packages

## Packages can contain
##              1.Modules
##              2. Packages

## If Module is a Package, it must have a value set for __path__.
## Therefore after you have imported a Module, you can easily see if that Module is a Package by inspecting __path__ attribute
## If its 1.Empty -> Module,  2.Non Empty -> Package



## IMP -
## Package has its code in __init__.py file
## When Package is imported, code inside __init__.py gets automatically executed
## A directory can be made as Package by adding __init__.py file in it

