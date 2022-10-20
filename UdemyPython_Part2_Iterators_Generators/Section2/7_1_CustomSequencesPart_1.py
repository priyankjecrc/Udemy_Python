## In this we shall be focusing on IMMUTABLE sequence types

## At very basic, Immutable type should support 2 things

## 1. Must return length of sequence ... by using __len__ ... (Technically we dont need that but we should implement it)
## 2. Must support index...by using __getitem__ (Imp one)   ........  If these 2 conditions are satisfied, we should be able to return value by square brackets[] and iterate through it
## __getitem__ at very basic takes in single Integer argument - the INDEX, it may also handle SLICE type argument

## __getitem__ -> must be used in a way so that it can 1. Return an element for valid index 2. Raise IndexError for invalid index


## Just few examples ... List implements __getitem__ method..


mylist = [1,2,3,4,5]
print(mylist[::-1])  ## [5, 4, 3, 2, 1] ... we are slicing here

print(mylist.__getitem__(0)) # 1
print(mylist.__getitem__(slice(None,None,-1)))  ## [5, 4, 3, 2, 1] ... How to do slicing when using __getitem__ is shown here

