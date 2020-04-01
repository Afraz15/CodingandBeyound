                    # LOCAL AND GLOBAL VARIABLE

def spam():
    global eggs         # calling the global vriable
    eggs = 'spam'       # changing the value of global variable

def bacon():
    eggs = 'bacon'      # this is a local variable or a function variable because it doesn't use "global"...
    print(eggs)         # test

def ham():
    print(eggs)         # this is calling the global variable since there is no variable present in the function...

eggs = 42
spam()                  # this is calling the spam() function...
print(eggs)

bacon()
print(eggs)             # it is calling the global variable if the test statement in the function is removed






