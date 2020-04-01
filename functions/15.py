                                # LOCAL AND GLOBAL SCOPE

def spam():
    global eggs                 # "global" is used to call a global variable and then we can change it's value within the function without making any new variable...
    eggs = 'edited'
        
eggs = 'original'               # "original" is the old variable value which we edited in the function
spam()                          # calling the function and once we call it , the value of the variable will be changed...
print(eggs)








