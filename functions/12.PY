                            # LOCAL AND GLOBAL SCOPE

def spam():
    eggs = 99         # 1. we can make variable of same name if they are used in seperate funcion just like this in 1.
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0        # 1. same variable...

spam()              # it won't get confused because there are two variables of same name in the whole program because they are in a seperate function...





