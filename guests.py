import sys

try:
    guest_names = []
    while True:
        print('Enter the name of guest ' + str(len(guest_names) + 1) 
            + ' or enter nothing to stop')
        name = str(input('> '))
        if(name == ''):
            break
        guest_names.append(name)

    print('The names of your guests are: ')

    for idx, name in enumerate(guest_names):
        print(str(idx + 1) + '. ' + name)

except KeyboardInterrupt:
    print()
    sys.exit()