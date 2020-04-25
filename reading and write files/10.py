                                #  CHECKING PATH VALIDITY

from pathlib import Path

win = Path.home()
print(win)

win1 = Path('C:\hello\eis.txt')

print(win.exists())

print(win.is_dir())

print(win1.exists())

print(win1.is_file())

print(win1.is_dir())

hi = Path('C:/')

print(hi.exists())

'''
these are some commands which are used to check if the path of a file or dictionary is correct or not

we can also check if a drive exists too

'''


