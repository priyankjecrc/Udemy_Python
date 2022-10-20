
## Garbage Collector destroys object based on 2 methods

## 1. Method1 - Reference Count to the Object becomes = 0
## 2. Method2 - Circular Referencce


## Case 1 : Method 1

## Python destroy the object based on reference count. If reference count to an object gets = 0, than python Garbage Collector will
## destroy that object..



## Case 2: Method 2

## ObjA -> ObjB -> ObjC -> ObjB

## If we drop ObjA, reference to ObjB will not be 0 because ObjC is still pointing to ObjB.
## Here Reference count concept will not work.
## There is a circular reference here. This causes memmory leak.
## Garbage Collector will identify Circular reference and destroys them

## By default Garbage Collector is on, you 'can' turn it off by gc.disable()

## Better watch video no 17 on Garbage Collector

import gc

gc.collect()
print(gc.get_objects())