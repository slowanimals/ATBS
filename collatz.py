#chapter 4 challenge, written by me

def collatz(x):
    if x % 2 == 0:
        return x // 2
    else:
        return (3 * x + 1)

try:
    num = int(input('Enter a number: '))
    while True:
        result = collatz(num)
        print(result, end = ' ')
        if result == 1:
            break
        num = result
    print()
    
except ValueError:
    print('invalid input')

