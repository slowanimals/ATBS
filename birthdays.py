# Chapter 7 exercise, written by me
import sys

birthdays = {'Paul' : 'Aug 29', 'Kaushali' : 'Jul 4', 'Chloe' : 'Jun 25'}

try:
    while True:
        print('Enter a name:')
        name = input('> ')
        if name == '':
            break

        if name in birthdays:
            print(name + '\'s birthday is on ' + birthdays[name] + '\n')
        else:
            print(name + " isn't in the database. Please enter their birth date: ")
            new_bday = input('> ')
            birthdays[name] = new_bday
            print('Successfully updated!\n' + name + '\'s birthday is on ' + birthdays[name] + '\n')


except KeyboardInterrupt:
    sys.exit()