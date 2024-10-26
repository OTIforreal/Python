#1.1 and 1.2

word = str(input())
listword = list(word.lower())

vowels = 'aeiou'
consonants = 'qwrtyplkjmnhgbvfdcxs'

repeat = []
count=1
count1=2

for i in listword:
    if i not in repeat:
     if count not in repeat:
           repeat.append((i,count))


list_vow = []
list_cons = []
list_symb = []

for char, count in repeat:
    if char in vowels:
        list_vow.append((char,count))
    elif char in consonants:
        list_cons.append((char,count))
    else:
        list_symb.append((char,count))



print(repeat)

print('vowels', list_vow)
print('cons:', list_cons)
print('symbols', list_symb)



