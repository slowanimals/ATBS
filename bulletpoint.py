# chapter 8 exercise, written by me
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

new_text = '\n'.join(lines)
pyperclip.copy(new_text)
print(new_text)

