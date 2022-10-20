
## Assignemnts

## 1. Normal Slicing Assignment.. Length on LHS and RHS may differ

l = [1,2,3,4,5,6]

l[1:3] = (10,20,30,40)  ## See how length is different
                         # This will cause mutation of list l.. Elements 2,3 will be replaced with 10,20,30,40

print(l) ## [1, 10, 20, 30, 40, 4, 5, 6]


## 2. Extended Slicing Assignment...Length on LHS and RHS must be same

l1 = [1,2,3,4,5,6]
l1[0:4:2] = [10,20] ## LHS and RHS must be of same length ... l1 is mutated
print(l1) ## [10, 2, 20, 4, 5, 6]


## Deleting a slice.... This will not work with Extended Slicing

l2 = [1,2,3,4,5,6]

l2[2:3] = []

print(l2) ## [1, 2, 4, 5, 6]

## Inserting a slice... This is different from Assignment.. Assignment was causing replacement.. This will not cause replacement
## This will not work with Extended Slicing

l3 = [1,2,3,4,5,6]

l3[2:2] = [10,20,30]

print(l3) ## [1, 2, 10, 20, 30, 3, 4, 5, 6]

