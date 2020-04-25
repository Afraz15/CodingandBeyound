                        # GLOB

from pathlib import Path

i = Path.home()

print(list(i.glob('.txt')))

'''
this will show the .txt files in home()

if there are more files with .txt then it will still display one file

'''
print(list(i.glob('.docx')))




