import sys
print('Inside Package5')

print(sys.modules.keys())
print(globals().keys())


from Package5.InnerPack import *  ## It means from InnerPack import everything
                                  ## But we have set __all__ in Innerpack...
                                  ## It means only those who are in __all__ will be allowed to import
                                  ## __all__ in innerpack has  - ['module11Func1', 'module12Func1', 'module13Func1']

print(sys.modules.keys())
print(globals().keys())