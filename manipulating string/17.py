                                # PARTITION

hi = 'hello and have a good day'

print(hi.partition('and'))      # this will seperate the and from the others...
print(hi.partition('llo'))      # this will seperate the oll from others even if it's part of another word...
print(hi.partition('o'))        # this will only seperate the first o if there are more then it will ignore them...

print(hi.split('o'))            # split() can do change all the o if used...













