                                # MAKING FUNCTION

print('Enter your birth month and see what your good at!!! :v')
print('Note! Dont use capital letters and if there is no answer then check your spelling...')

def fish(blue):
    if  blue == 'january':
        return 'Watching Netflix' 
    elif  blue == 'febuary':
        return 'Dowing shots' 
    elif  blue == 'march':
        return 'Sleeping' 
    elif  blue == 'april':
        return 'Spending money' 
    elif  blue == 'may':
        return 'Not going to the gym' 
    elif  blue == 'june':
        return 'Shopping' 
    elif  blue == 'july':
        return 'Drink juice only' 
    elif  blue == 'august':
        return 'Being sassy' 
    elif  blue == 'september':
        return 'Nothing'  
    elif  blue == 'octuber':
        return 'Always being late' 
    elif  blue == 'november':
        return 'Looking up to others' 
    elif  blue == 'december':
        return 'Being dramatic' 

month = input() 
answer = fish(month)
print(answer)

