import random, sys, time

WIDTH = 100

try:
    matrix = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                matrix[i] = random.randint(1,2)
        
            if matrix[i] == 0:
                print(' ', end = '')
            else:
                print('⚛︎', end = '')
                matrix[i] -= 1
        print()
        time.sleep(0.02)
except KeyboardInterrupt:
    sys.exit()