
## Some more application of __all__
## Referring to Package4

from Package4 import *  ## means - from Package import Module1 ... look into __init__ file of Package4

Module1.printSomething1()
## Module2.sampleFunc1() ##--- Will cause error



