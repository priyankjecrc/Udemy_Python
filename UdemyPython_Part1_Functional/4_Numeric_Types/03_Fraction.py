import math
from fractions import Fraction

a = Fraction(3,4)
b = Fraction(-3,4)
print(a,b) ## 3/4 -3/4

a = Fraction("10")
b = Fraction("0.2")

print(a,b) ## 10 1/5

print(Fraction("4.1")) ## 41/10
print(Fraction(4.1)) ## 2308094809027379/562949953421312   ... but why ? This is a caveat.. because 4.1 is not exactly stored as 4.1(in float)

print(Fraction(0.2)) ## 3602879701896397/18014398509481984 .... but why ? This is a caveat...because 40.2 is not exactly stored as 0.2(in float)


## Using limit_denominator we can find approximately equal fraction

x = Fraction(math.pi) ## 884279719003555/281474976710656
print(x.limit_denominator(100)) ## 311/99

print(Fraction(0.2).limit_denominator(1)) ## 0
print(Fraction(0.2).limit_denominator(2)) ## 0
print(Fraction(0.2).limit_denominator(3)) ## 1/3
print(Fraction(0.2).limit_denominator(4)) ## 1/4
print(Fraction(0.2).limit_denominator(5)) ## 1/5


## a = Fraction(1,0) ## ZeroDivisionError: Fraction(1, 0)