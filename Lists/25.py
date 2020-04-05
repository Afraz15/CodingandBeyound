                                # IMPORT COPY
import copy

spam = [1, 2, 3, 4, 5]
cheese = copy.copy(spam)        # this is how we copy a value of another variable
print(cheese)

cheese[2] = 'hello'             # this will only do the change in cheese variable
print(cheese)               
print(spam)








