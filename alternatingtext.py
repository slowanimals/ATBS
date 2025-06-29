# chapter 8 exercise, written by me

import pyperclip
text = pyperclip.paste()
new_text = ''
make_upper = False
for c in text:
    if make_upper:
        new_text += c.upper()
    else:
        new_text += c.lower()
    make_upper = not make_upper

pyperclip.copy(new_text)
print(new_text)