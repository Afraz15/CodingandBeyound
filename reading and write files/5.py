                            # ABSOLUTE DIRECTORY

from pathlib import Path

print(Path.home())

print(Path(r'C:\Users\AL RAFIO').is_absolute())
print(Path(r'hello\hi\bye').is_absolute())
print(Path(r'C:\hello').is_absolute())

'''
if the path is correct then it will answer true else false

if some path is correct then it will also be true just like the last statement

'''

