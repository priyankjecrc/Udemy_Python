
import math  as r_math   ## IMP - Here in "globals()" reference will be added as Key - r_math, Value - <module 'math' (built-in)>
print(r_math)            ## "math" will not exists in globals()
                         ## but in sys.modules it will added as Key - math, Value - <module 'math' (built-in)>

print(globals()['r_math']) ## <module 'math' (built-in)> - a module object

## =================================================================================================

from math import sqrt   ##  IMP - Here in "globals()" reference will be added as Key - sqrt, Value - <built-in function sqrt>
print(sqrt)             ## but in sys.modules it will added as Key - math, Value - <module 'math' (built-in)>

print(globals()['sqrt']) ## <built-in function sqrt>


## =================================================================================================

from math import sqrt as r_sqrt  ## IMP - Here in "globals()" reference will be added as Key - r_sqrt, Value - <built-in function sqrt>
print(r_sqrt)                    ## but in sys.modules it will added as Key - math, Value - <module 'math' (built-in)>


print(globals()['r_sqrt'])  ## <built-in function sqrt>


## =================================================================================================

from math import *  ## All the symbols defined in math will be added in globals()
                    ## but in sys.modules it will added as Key - math, Value - <module 'math' (built-in)>


## IMP in all the cases of import we mentioned above, math module will anyway will be loaded completely. There is no partial
## loading of math module, for eg in case from math import sqrt - entire math module will be loaded in sys.modules


## Things may be different with "Packages" but with simple modules this is the behaviour


## =================================================================================================

## Caveats

from cmath import *
from math import *   ## Here for eq - in globals() math's sqrt will step on cmath's sqrt
                     ## that's why many don't like import * as it can lead to bugs


## Which is preferred -

# (1). from math import sqrt or (2). import math and then use math.sqrt  --- well not much of difference
## in case (1). it can directly look for sqrt in globals(), while in (2)nd case it will look first for math in globals and then in math it will
## out for sqrt. it just that one extra lookup is added in case 2...... But math.sqrt is good for users readibility

## It is always better to use import math. There are some reasons stated in video 134 Reloading Modules after 14.18.
## For now just stick with the fact that its always better to use import math, instead of import math.sqrt






