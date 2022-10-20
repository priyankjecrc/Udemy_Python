import sys
print('inside innerPack')

print(sys.modules.keys())
print(globals().keys())



from Package5.InnerPack.Module11 import *
print(sys.modules.keys())
print(globals().keys())

from Package5.InnerPack.Module12 import *
print(globals().keys())

from Package5.InnerPack.Module13 import *
print(globals().keys())


__all__ = Module11.__all__ + Module12.__all__ + Module13.__all__


print(sys.modules.keys())
print(globals().keys())