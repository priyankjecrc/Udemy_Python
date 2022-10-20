
import TestModule    ##  This is TestModule
del globals()['TestModule']  ## We are deleting reference just from globals. It means that it is still there in sys.modules

import TestModule    ## TestModule will not be executed again, because we have just deleted its reference from globals
                     ## and it is still there in sys.modules. Its reference will be put again in globals