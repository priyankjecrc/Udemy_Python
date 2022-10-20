print('This is Package4')


from Package4 import Module1
from Package4 import Module2
from Package4 import Module3

## Above from statement will lead to import of Module1, Module2, Module3
## Out of all imported Module, we just want  Module1 to be exported

__all__ = ['Module1']



