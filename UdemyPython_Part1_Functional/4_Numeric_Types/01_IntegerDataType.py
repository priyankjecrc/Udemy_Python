
## How many memmory is used to store an integer
import sys
import time

print(sys.getsizeof(1)) ## 28 Bytes

def calc(a):
    for i in range(100000000):
        a*2

## Piece of code to show working of time.perfcount()

start = time.perf_counter()
calc(10)
end = time.perf_counter()
diff = end-start
print(diff) ## 3.3053894

## Floor Division

print(155//4) ## 155 = 4*38 + 3... O/P -> 38

print(-155//4) ## -155 = 4 * (-39) + 1.... O/P -> -39

## Modulo Operator

print(155%4) ## O/P -> 3

print(-155%4) ## O/P -> 1

import math

print(math.floor(155/4)) ##  38
print(math.floor(-155/4)) ## -39
