# chapter 4, written by me
import time, sys

indent = 0
increasing = True

try:
    while True:
        for i in range (1,10):
            print('-' * (i*i))
            time.sleep(0.1)
            
        for i in range (10, 1, -1):
            print('-' * (i*i))
            time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()