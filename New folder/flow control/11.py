                                # CONTINUE STATEMENT
while True:
    print('Who are you ?')
    name = input()
    if name != 'joe':
        continue    
    print('Hello,Joe. What is the password?')
    password = input()
    if password =='swordfish':
        break
print('Access granted.')

