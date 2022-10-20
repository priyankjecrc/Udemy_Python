
## Was able to understand only half of video - 135 using __main__


print(f'module Name = {__name__}') ## module Name = __main__... Why __main__ ? why not 06_Using__main__.py

import TestModule4  ## module Name = TestModule4...
                    ## In TestModule4 we have this statement --- print(f'module Name = {__name__}')
                    ## because we are calling TestModule4 here, the __name__ of TestModule4 will show as TestModule4 and not as __main__
                    ## If we look value of __name__ from within TestModule4, then it will come as __main__

## If module is run from the module file.. eg - if I run 06__Using__main__.py module from inside this module only
## than __name__ is set to main. Therefore we can check by looking into __name__ value, if module was run from same file or from some other file

if __name__ == '__main__':
    print('Module executed')

## this kind of leverage is used if we wish to run module from module itself vs we wish to module from some other place else
## For eg - if I wish to print - 'Module executed' only when I run module from module itself then i can use if __name__ == '__main__'
## We use if __name__ == “__main__”  to prevent (certain) code from being run when the module is imported.