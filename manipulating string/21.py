                            # TYPES OF STRIPS

h = 'hello world       '
j = '       hello world'
k= '    hello world    '

l = [ h, j, k]

i = 1

while i < 3:
    print(str(l[i]).strip())    # this will strip all the spaces from both sides
    print(str(l[i]).lstrip())   # this will strip all the spaces present in the left side
    print(str(l[i]).rstrip())   # this will strip all the spaces form right side
    i = i + 1








