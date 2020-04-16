                                # ISUPPER AND USLOWER

print('how are you feeling today?')

feel = input()

if feel.lower() == 'great':                 # adding some code like lower() will help the program that the input can be lower or upper case...
    print('i\' feeling great too')
else:
    print('i hope you have a nice day')

mood = input()

if mood.upper() == 'GOOD':                  # so it seem like if we use upper case or lower ; the value which we equal to should be of the same case or it won't work...
    print('i\'m feeling good too!! ')
else:
    print('i hope you have a nice day ')


if mood.upper() == 'good':                  # LIKE THIS ONE...IT WILL PRINT THE ELSE STATEMENT
    print('i\'m feeling good too!! ')
else:
    print('i hope you have a nice day ')









