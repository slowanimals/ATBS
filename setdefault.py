# Chapter 7 exercise, written by me

sentence = 'The quick brown fox jumps over the wooden fence'
count = {}

for letter in sentence:
    x = letter.upper()
    count.setdefault(x, 0)
    count[x] += 1

print(count)