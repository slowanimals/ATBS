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

import pyperclip
import re

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


#TODO (OPTIONAL) find addresses
address_re = re.compile(r'''(
                            (\d+)\s+ # number 1
                            ((N|E|S|W)\s+)?
                            ([a-zA-Z0-9\s]+)\s+ # street name 2
                            ((St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Ln|Lane|Dr|Drive)\.?)\s* # street type 3
                            ((Apt|Suite|\#)\.?\s*\d+)?\s*  # apt/suite number (optional) 4
                            ([a-zA-Z\s]+,)\s+# city 5
                            (\s*[A-Z]{2})\s+ # state 6 
                            (\s*\d{5}(-\d{4})?) #zip code 7
)''', re.VERBOSE)

# TODO: Find matches in clipboard text.
matches = []
text = pyperclip.paste()
raw_phone_numbers = phone_re.findall(text)
raw_emails = email_re.findall(text)
raw_address = address_re.findall(text)

'''
1690 Barton Rd Suite 101
Redlands, CA 92373
'''

#rejoin
for groups in raw_phone_numbers:
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)

for groups in raw_emails:
    matches.append(groups)

for groups in raw_address:
    address = ' '.join([groups[1], groups[2], groups[3]])
    if groups[6]:
        address += ' ' + groups[6]
    city = groups[8].strip(',')
    state = groups[9].strip()
    zip = groups[10].strip()

    result = f'{address} {city}, {state} {zip}'
    matches.append(result)
    



# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers, emails, or addressses found')
