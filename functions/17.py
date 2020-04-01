                        # LOCAL AND GLOBAL SCOPE

def spam():
    print(eggs)            # this will cause an error because in the function , it says to print the "eggs" variable but since there is no variable assigned before it but instead after it as a result it cann't go to the global variable because there is a local variable in the function but in an unorder way...
    eggs = 'spam local'

eggs = 'global'
spam()









