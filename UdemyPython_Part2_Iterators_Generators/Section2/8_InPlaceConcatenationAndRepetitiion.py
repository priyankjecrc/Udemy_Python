
## will discuss about += operator and *= operator

a = 10
a = a+10 ## can be given as a += 10

list1 = [1,2,3]
print(id(list1))  ## 2596132311432

list2 = [4,5,6]

list1  = list1+list2
print(id(list1))  ## 2596132311432... it changes because we are reassigning to list1

## if we do list1 += list2... we will think that it will be equivalent to list1 = list1 + list2
## but its not....here for mutables += will cause mutation

list3 = [1,2,3]
list4 = [4,5,6]

print(id(list3)) ### 2716060438920

list3 += list4    ## [1,2,3,4,5,6]
print(id(list3))  ## 2716060438920... We can see that memmory add is not changed.. Because it has mutated list3

## For Immutables += will have same effect as tuple1 = tuple1 + tuple2... first tuple1 + tuple2 will create a new object and this will be
## assigned to tuple1. Same case will not happen for mutables

## For *= .. same behaviour will happen as explained above for +=