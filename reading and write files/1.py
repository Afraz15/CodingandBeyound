                                # BACKSLASH ON WINDOWS

from pathlib import Path

files = ['account.txt', 'hello.css', 'bye.exe']

for name in files:
    print(Path(r'C:\users\al',name))


