                            # LOCAL AND GLOBAL SCOPE
def hi():
    bro = "none"  # This is a local variable/scope
    print(bro)

print("bro") # remove the ""        # it will result in error since it is not a global variable

hi()              # now we are using the function where the local variable/scope is located and it will work...


