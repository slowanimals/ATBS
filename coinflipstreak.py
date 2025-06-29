# Chapter 6 exercise, written by me

import random

num_of_streaks = 0

for i in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    result = [0] * 100
    for i in range(len(result)):
        result[i] = random.randint(0,1)

    # Code that checks if there is a streak of 6 heads or tails in a row
    counter = 0
    for i in range(1,len(result)):
        if result[i - 1] == result[i]:
            counter += 1
        else:
            counter = 0
        
        if counter == 6:
            num_of_streaks += 1
        
print('Chance of streak: %s%%' % (num_of_streaks / 100))