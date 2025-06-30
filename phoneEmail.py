#chapter 9 project
'''
your phone number and email address extractor will need to do the following:
Get the text from the clipboard.
Find all phone numbers and email addresses in the text.
Paste them onto the clipboard.
Now you can start thinking about how this might work in code. The code will need to do the following:

Use the pyperclip module to copy and paste strings.
Create two regexes, one for matching phone numbers and one for matching email addresses.
Find all matches (not just the first match) of both regexes.
Neatly format the matched strings into a single string to paste.
Display some kind of message if no matches were found in the text.
'''

import pyperclip, re

phone_re = re.compile(r'''(
                      (\d{3}|\(\d{3}\))?  # area code 1
                      (\s|-|\.)?  # separator 2
                      (\d{3})  # first three digits 3
                      (\s|-|\.)?  # separator 4
                      (\d{4}) # last four digits 5
                      (\s*(ext|x|ext\.)\s*(\d{2,5})) ?  #extension 6
                      )''', re.VERBOSE)

# TODO: Create email regex.
email_re = re.compile(r'''
                      [a-zA-Z0-9_%+-]+ # username 
                      @ # @
                      [a-z0-9.-]+# Domain
                      \.[a-zA-Z]{2,4}# . something
                      ''', re.VERBOSE)

# TODO: Find matches in clipboard text.
matches = []
text = pyperclip.paste()
raw_phone_numbers = phone_re.findall(text)
raw_emails = email_re.findall(text)


#TODO (OPTIONAL) find addresses
raw_address_re = re.compile(r'''(
                            # number
                            # street name
                            # street type
                            # 
                            
)'''
)




#rejoin
for groups in raw_phone_numbers:
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)

for groups in raw_emails:
    matches.append(groups)








# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found')
