                                            # VALID INPUT TYPE

while True:
    print('enter your age')
    age = input()
    try:
        age = int(age)
    except:
        print('enter your age in numbers')
        continue
    if age < 1:
        print('enter your age in positive number')
        continue
    break
print(f'your age is {age} ')

'''
to just have the value in num we have to use these type of mathods

'''






