            # GUESS A NUMBER PROGRAM

import random
secretNumber = random.randint(1,20)
print('I am thinking of a numver between 1 and 20.')
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # if the condition is correct the loop control will execute this.
if guess == secretNumber:
    print('Good job! You guessed my number in '+str(guessesTaken)+' guesses!')
else:
    print('Nope, The numver i was thinking of was '+str(secretNumber))













