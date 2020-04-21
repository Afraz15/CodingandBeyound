                        # CHECKING IF IT'S A PHONE NUMBER

def phone(text):
    if len(text) != 12:
        return False
    for i in range (0,3):       # this 'i' means that i want to count from 0 to 3 and set i to current loop which also means that each time the loop will run it will change the value of 'i'...
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True

print(phone('444-555-4566'))











