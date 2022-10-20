
## Break - This will break out of the loop and terminates the loop immediately
## Continue - The current iterations we are into right now, just skip everything after the Continue statement and go back to the beginnign of the loop
##            rerun some test and if its True, continue the running. Basically it bails out of current iteration


a = 0
while a<10:
    a = a+1
    if(a%2 == 0):  ## As any number divisible by 2 comes, conitnue will get hit and everything after continue will be skipped.
        continue   ## the control will go to the begining of the loop.
    print(a)



## Explaining While - else ... This is a type of statement
## Else will execute only when while condition becomes False

b = 0
while b<10:     ## When condition mentioned in while becomes False, else will execute... Just like in if else statement
    if(b==7):  ## But if 'break' is encountered before condition could turn False, it will break out of loop and else will never be executed
        break
    b = b+1
else:
    print(f'printing value of b = {b}')

print(f'Value of b after exiting the while - else loop because of break condition = {b}')  ## 7