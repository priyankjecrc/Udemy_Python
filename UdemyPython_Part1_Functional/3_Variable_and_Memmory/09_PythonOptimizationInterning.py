
## First 2 minutes of video - Video 25 Python Optimization: Interning

## Interning is a concept where python decides if something can be used as shared reference
## for eg - c python has integer range - (-5 to 256). If an integer falls in this range it will be considered for shared reference,
## but if any value is chose beyond this range, it will not be used for shared reference

## Likewise not all the Strings are utilized for shared reference(also called as Interned)

## But we can force interning by using sys.intern() method

import sys

str1 = sys.intern('abc')  ## Forcing interning of String
str2 = sys.intern('abc')  ## Forcing interning of String... we can't do str2 = 'abc'.. we will have to use sys.intern
str3 = 'abc'

print(id(str1), id(str2), id(str3)) ## 2529164519280 2529164519280 2529164519280 - here all are same BUT, id(str3) might return different value

print(str1 == str2) ## True - it compares character by character and it takes longer.


## Imagine if strings are very very long than this type of comparison will take a lot of time
## A good option will be - if 2 strings that we intend to compare are very long but equal, then its better to intern them
## and compare memmory address like - str1 is tr2

## For eg below example

a = 'a very long string' * 10000000
b = 'a very long string' * 10000000

print(id(a), id(b)) ## 1352554115136 1352734158912 - different values and comparing by a == b will take a lot of time

c = sys.intern('a very long string' * 10000000)
d = sys.intern('a very long string' * 10000000)

print(id(c), id(d)) ## 2087534215232 2087534215232 - same id

## and for comaprison, we can do something like

print(c is d) ## True