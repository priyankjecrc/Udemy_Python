

myseq = [1,2,3,4,5,6]

## Suppose I wish to reverse myseq

revseq = myseq[::-1] ## downside is , it will make an new copy

## Other way to reverse the sequence

for i in range(len(myseq)):
    print(myseq[len(myseq)-i-1])

## for better visibility we can use following way

for i in reversed(myseq):  ## This will not create a copy.. it will just iterate it
    print(i)


for k in reversed(*['priyank']):
    print(k)

## k
## n
## a
## y
## i
## r
## p


## Now to Reverse User Defined Objects we can't directly used reversed()
## Because when we call reversed() on an custom object
## 1. It will look out for __reversed__ method
## 2. If __reversed__ is not there, it will use __getitem__ and __len__ to create iterator for us

## Therefore we can say that - To reverse user-defined objects the class must do one of the following:
## 1. Implement __len__()  and __getitem__()  methods
##                   OR
## 2. Implement __reversed__() method


