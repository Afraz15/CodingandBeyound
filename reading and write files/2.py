                        # USING / OPERATOR

from pathlib import Path

hi = Path('spam') / 'hello' / 'bye'
I = Path('spam') / Path('hello/bye')
Ii = Path('spam') / Path('hello', 'bye')

print(hi)
print(I)
print(Ii)

'''
these are the type of mathods which we can use to add a path with other file

'''
i1 = Path('spam') / 'hello'
i2 = Path(i1) / 'bye'
i3 = Path(i2) / 'wb'
print()
print(i1)
print(i2)
print(i3)

'''
this is how we are making 
