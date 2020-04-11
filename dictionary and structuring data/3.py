                                # BIRTHDAY MONTH

birth = {'Austin':'Jan 1', 'Alice':'Feb 29', 'Arial':'Nov 29'}

while True:
    print('Enter your name to see your birthday...(or enter blank to quit')
    name = input()
    if name == '':        # if name is empty then it's true...
        break
    
    if name in birth:
        print(birth[name] + ' is the brithday of ' + name)
    else:
        print('I dont have information about' + name)
        print('when is ' + name + 'birthday?')
        bd = input()
        birth[name] = bd    # here is where we add a new dictionary value but the value of the varaible should not be the same in the dictionary like eve:'Jan 1' <- this is a no no...
        print('data updated!!')












