# ch 9 exercise
import re

pattern = re.compile(r'(\d{3})-\d{3}-\d{4}')
sample = pattern.search('My phone number is 918-829-2547')
print(sample.groups())
print()

pattern2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
sample2 = pattern2.search('My phone number is (415) 555-4242.')
print(sample2.groups())
print()

pattern3 = re.compile('Cat(erpillar|ch|egory)')
sample3 = "Catch me if you're a Caterpillar!"
print(pattern3.findall(sample3))
print()

vowels = re.compile(r'[aeiouAEIOU]')
print(vowels.findall('EWW don\'t eat that BABY FOOD!'))
print()

pattern4 = re.compile(r'\$\d+')
sample4 = 'I have $1000 in my btc wallet'
result = pattern4.sub(r'CENSORED', sample4)
print(result)
print()