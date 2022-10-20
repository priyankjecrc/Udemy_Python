
## In the video I have skipped Base part


a = int(10)
b = int(10.5)

print(a,b) ## 10, 10

a = int(-10)
b = int(-10.5)

print(a,b) ## -10 -10

a = int(True)
b = int(False)
print(a,b) # 1 0

a = int("1000") ## a = 1000
b = int("10.5") ## Value Error: invalid literal for int() with base 10: '10.5'