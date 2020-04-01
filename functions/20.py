                            # TRY AND EXCEPT

def spam(divide):
    return 22 / divide

try:
    print(spam(3))
    print(spam(22))
    print(spam(0))          # the program will show error in this statement because it is divided by zero and when it jumps to the except statement ; it won't go back to execute the remaining statements...
    print(spam(12))
    print(spam(8))
except ZeroDivisionError:
    print('Error: invalid argument')        # argument means the value which we write between the circle brackets "()"...











