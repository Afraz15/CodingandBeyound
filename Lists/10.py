                                                # LISTS

games = []                                      # This is an empty list variable

while True:

    print('Enter the name of your fav game' + str(len(games) + 1) + '(Or enter nothing to stop.):')    # this "str..." will count the numbers of list values and enter their number there and add 1 in it so it look like this... fav game 1 then 2 then 3 and so on...

    name = input()                               

    if name == '':                               # 1. These quotes means empty or when we just type enter...
        break                                    # 2. As a result the loop will break...

    games = games + [name]                       # This will add the files of "name" into games which will look like this ['none', 'none', (the value present in the name)]

print('The name of your fav games are...')
 
for name in games:
    print('' + name)








