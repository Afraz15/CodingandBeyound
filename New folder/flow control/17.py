                                # IMPORT SYS

import sys

while True:
    print('Type exit to exit.')
    response = input()      
    if response == 'exit':
        sys.exit()                  # sys.exit is used to exit a program
    print('You typed ' + response + '.')


