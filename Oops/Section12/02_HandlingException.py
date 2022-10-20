

def func1():
    raise ValueError('This function throws Value Error')

try:
    func1()
except ValueError as ex:   ## ex is instance of error raised in func1() ## Order in which error has to be specified should be from Most Specific to
   print('Handling Value Error', repr(ex))         ## Least Specific..
                                                    ## instead of 2 lines we can also do something like except(ValueError,IndexError) as ex
except IndexError as ex:
    print('Handling Index Error', repr(ex))

else:
    print('No Exception occured')                  ## It needs at least one 'except' to present
                                                   ## It is executed only if no exception occurs. Here as exception is occuring, therefore
                                                   ## it will not execute. Else block can't be placed after finally
finally:
    print('Running Finally')                      ## This will be executed in every case. It doesn't matter if exception occured or not
                                                  ## It is guaranteed to run
                                                  ## In case error propagates, finally will be executed first and then propagation will happen



