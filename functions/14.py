                        # LOCAL AND GLOBAL SCOPE

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon Local'        # only assigned a value to a variable
    spam()                      # call a whole funtion...
    print(eggs)                 # calls the variable present in the function


eggs = 'global'
bacon()
print(eggs)

# first it will go to bacon() then print value of eggs if there is a varible present in the function then it will print the value of variable "eggs" which is present outside of the function...






