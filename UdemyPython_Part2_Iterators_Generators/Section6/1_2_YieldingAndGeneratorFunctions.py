import math


def facto(n):
    for i in range(n):
        yield math.factorial(i)




fact4 = facto(4)

print(next(fact4))  ## 1 ... factorial 0
print(next(fact4))  ## 1 ... factorial 1
print(next(fact4))  ## 2 ... factorial 2
print(next(fact4))  ## 6 ... factorial 3
## print(next(fact4))  ## StopIteration


fact6 = facto(6)

print(next(fact6))  ## 1 ... factorial 0
print(next(fact6))  ## 1 ... factorial 1
print(next(fact6))  ## 2 ... factorial 2
print(next(fact6))  ## 6 ... factorial 3 ... still not exhausted

for k in fact6:
    print(k)

## 24 ... factorial 4
## 120 ... factorial 5


## A Good Example

fact8 = facto(8)

print(list(fact8))  ## [1, 1, 2, 6, 24, 120, 720, 5040]

## Can we fix this exhaustion of Generator problem .... Will be discussed later


## Another good example... using Enumerator ... look at the problem

def squares(n):
    for i in range(n):
        yield i**2

sq = squares(5)
enum1 = enumerate(sq)   ## Ans to below Question - because Enumerator is lazy. It hasn't iterated through sq yet
                        ## By the time Enumerator started, sq had already done 2 hops. Kind of this problem can be solved as shown in notebook 2_1

print(next(sq)) ## 0
print(next(sq)) ## 1

print(list(enum1))      ## [(0, 4), (1, 9), (2, 16)]
                        ## Why [(0, 4), (1, 9), (2, 16)] and why not [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)] ???







