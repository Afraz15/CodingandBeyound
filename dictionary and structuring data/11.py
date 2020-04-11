                            # TIC TAC TOE PROGRAM

board = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M': 'X', 'mid-R': '', 'low-L': '', 'low-M': '', 'low-R': 'X',}        # changing the values of the dic value, we can make a tic tac toe matrix...

def draw():
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']   )
    print('_+_+_')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']   )
    print('_+_+_')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']   )
    print('_+_+_')
    
print(draw())








