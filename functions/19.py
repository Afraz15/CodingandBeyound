                            # TRY AND EXCEPT

def spam(divide):
    try:                        # if there is a chance that this function or statement can cause an error then it is put into "try" so that it won't cause the whole program to stop it's execution...
        return 33 / divide
    except ZeroDivisionError:   # this is used if the division is zero...
        print('Error: invalid argument.')

print(spam(32))
print(spam(5))
print(spam(-2))
print(spam(0))









