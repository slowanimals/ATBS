# chapter 4, written by author
import time, sys
indent = 0
increasing = True


while True:
    print(' ' * indent, end = '')
    print('********')
    time.sleep(0.0)

    if increasing:
        indent += 1
        if indent == 20:
            increasing = False
    else:
        indent -= 1
        if indent == 0:
            increasing = True
