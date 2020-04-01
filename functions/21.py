                        # ZIG ZAG PROJECT

import time, sys                            # calling the time and sys mode
indent = 0                                  # number of spaces
indentIncreasing = True                     # if the indent/spaces are increasing or not

try:
    while True:
        print(' ' * indent, end='')         # ''*indent is a formula to get the correct number of spaces
        print('********')
        time.sleep(0.01)                     # speed of the zig zag

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False

        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
                sys.exit()










