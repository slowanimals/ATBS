# Chapter 6 exercise, written by me

def comma(l):
    if len(l) == 0:
        return None

    x = '' + l[0] #beginning
    
    for i in range(1, len(l) - 1): #middle
        x += ', ' + l[i]
    
    x += ', and ' + l[len(l) - 1] #end

    return x


spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = []

print(comma(spam))
print(comma(spam2))

