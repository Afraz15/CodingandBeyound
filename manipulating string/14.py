                                # USING ISX() IN LOOP

while True:
    print('enter your password (letters and numbers only)')
    i = input()
    if i.isalpha():
        break
    else:
        print('enter your password in letters and numbers only please')
        i = input()
        if i.isalpha():
            break
        else:
            print('try again after refreshing web page')
            break
















