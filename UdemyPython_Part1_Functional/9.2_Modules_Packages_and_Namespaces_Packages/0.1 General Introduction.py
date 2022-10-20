
## VV IMP
##  When importing a file, Python ONLY searches the directory that the entry-point script is running from and sys.path which includes locations such as the package installation directory

## Above thing can be demonstrated with an example

## We have TestPack as package, and firstOne and secondOne as modules in it.
## firstOne imports secondOne

## Case 1
## when in firstOne we have statement like - import secondOne
'''

from TestPack import firstOne ## Will give Error - ModuleNotFoundError: No module named 'secondOne', because of reason mentioned above
                              ## Therefore it is absolutely essential to give complete path while importing
                              ## But This also has a problem. It might lead to cycle...
                              ## Problem is mentioned in - 1.5 Understanding Packages_Part5.py


'''


## Case 2
## When in firstOne we have statement like - import TestPack.secondOne

'''

from TestPack import firstOne ## No Error.. but still issue is there..I cant access function inside secondOne

## firstOne.secondOne.secondFunc() ## AttributeError: module 'TestPack.firstOne' has no attribute 'secondFunc'
                      ## because in firstOne we still can't use secondOne. Its happening because in firstOne globals() we have
                      ## TestPack as key
                      
firstOne.TestPack.secondOne.secondFunc() ## inside second Func .. .this will work

'''

## Case 3
## When in firstOne we have statement like - import TestPack.secondOne as snd

'''
from TestPack import firstOne

firstOne.snd.secondFunc() ## inside second Func...
                          ## Worked because when we imported firstOne, in firstOne we have access to variable snd 
                          ## and snd has access to secondFunc()
                          
'''

## Case 4
## When in firstOne we have statement like - from TestPack.secondOne import *

'''

from TestPack import firstOne
firstOne.secondFunc()  ## inside second Func

'''