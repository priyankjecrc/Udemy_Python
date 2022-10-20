
## We are going to look into Generator Comprehension..
## Also we will be looking into List Comprehension vs Generator Comprehension

## List comprehension

squareList = [i**2 for i in range(4)]   ## we use square bracket and it returns a list
print(squareList) ## [0, 1, 4, 9]       ## Here
                                        ## 1. Evaluation is eager
                                        ## 2. It is an iterable..
                                        ## 3. All objects are created right away
                                        ## 4. Iteration is faster
                                        ## 5. Entire collection is loaded into memory

squareGen = (i**2 for i in range(4))    ## We use normal brackets and it returns a generator... Think of this as - yield i**2
print(list(squareGen)) ## [0, 1, 4, 9]  ## 1. Evaluation is lazy
                                        ## 2. It is an Iterator..hence it gets consumed
                                        ## 3. Objects creation is delayed until requested by next()
                                        ## 4. Iteration is slower because of above reason
                                        ## 5. Only a single item is loaded at a time