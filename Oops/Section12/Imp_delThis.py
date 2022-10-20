
## Here Block2 will not execute as we have raised an error in block 1 last line and that error is not caught. Therefore error will propagate
## and Block2 will not execute


## Block1
try:
    raise ValueError()
except ValueError as ex:
   print('inside first try')
   try:
       raise TypeError()
   except TypeError as ex:
       raise KeyError() from None


## Block 2
try:
    raise ValueError()
except ValueError as ex1:
    print('inside second try')