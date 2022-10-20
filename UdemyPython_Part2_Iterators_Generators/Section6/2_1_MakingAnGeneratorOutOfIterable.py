
## What is the problem so far with Generators : They gets exhausted, hence we can't use them again

## Above problem can be solved exactly like we solved the same problem in iterators

def squares(n):
    for i in range(n):
        yield i**2

class Squares():
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return squares(self.n)  ## Solution to above problem. Every time __iter__ is called it will call squares()


## Initially

sq = squares(5)

for i in sq:
    print(i)

## 0
## 1
## 4
## 9
## 16

for i in sq:  ## Will not do anything since sq is exhausted
    print(i)

### ==========================================================================================================

## Now

SQ = Squares(5)

for i in SQ:
    print(i)

## 0
## 1
## 4
## 9
## 16

for i in SQ:  ## Now this is working.. because everytime we iterate, than everytime __iter__ is called and becaseu of this everytime squares()
    print(i)  ## function will be called

## 0
## 1
## 4
## 9
## 16

## Solving problem of notebook 1_2

## problem

sq_8 = squares(8)

sq_enum1 = enumerate(sq_8)
sq_enum2 = enumerate(sq_8)

print(list(sq_enum1)) ## [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49)]
print(list(sq_enum2)) ## [] ... because sq_8 has been exhausted

## Solution

SQ_8 = Squares(8)
SQ_Enum1 = enumerate(SQ_8)
SQ_Enum2 = enumerate(SQ_8)

print(list(SQ_Enum1)) ## [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49)]
print(list(SQ_Enum2)) ## [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49)]
