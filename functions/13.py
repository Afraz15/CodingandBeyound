                        # LOCAL AND GLOBAL SCOPE

def spam():
    print(eggs)

eggs = 34       # this is a global variable because it is... outside? 

spam()          # since there is no variable named "eggs" in the function it will use the variable outside of the function...

print(eggs)



