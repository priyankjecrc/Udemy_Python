## Some interesting Part after - 33 mins of video -> 28. List Comprehensions - Coding

## Comprehension have their own Local scope just like Functions

sq = [ i**2 for i in range(10)]

## There are 2 phases - Compilation and Runtime..
# When RHS is compiled - Python creates a Temporary Function that will be used to evaluate the comprehension ie  [ i**2 for i in range(10)]

## Example of Nested Comprehension

##          -----------------------   shown upto ---  -> this is closure as well
someList = [[ i*j for j in range(5)] for i in range(5)]
print(someList) ## [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]]