"""
"Task 1

There is a list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

Print all the elements that are less than 5. "
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for int in a:
    if int<=5:
        print(int)
"""
"""
"Task 2 

The lists are given: 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]; 

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]. 

You need to return a list that consists of elements that are common to these two lists. 

 "
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for numb in a:
    for numb2 in b:
     if numb == numb2:
        print(numb2)
"""
"""
numbs = list(set(a) & set(b))

print (numbs)
"""

"""Task 3 

Sort the dictionary by value in ascending and descending order. 

 

Import the necessary module and declare the dictionary: 

import operator 

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} """
import operator
"""


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def valuable(item):
    return item[1]

sortedvalsasc = dict(sorted(d.items(), key=valuable))
sortedvalsdesc = dict(sorted(d.items(), key=valuable, reverse=True))



print(sortedvalsasc)
print(sortedvalsdesc)
"""
"""Task 4 

Write a program to merge several dictionaries into one. 

Let's say here are our dictionaries: 

dict_a = {1:10, 2:20} 

dict_b = {3:30, 4:40} 

dict_c = {5:50, 6:60} """
"""
dict_a = {1:10, 2:20}

dict_b = {3:30, 4:40}

dict_c = {5:50, 6:60}

alldict = dict_a | dict_b | dict_c

print(alldict)
"""
"""Task 5 

Find the three keys with the highest values in the dictionary my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}. """
"""
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

def valuable(item):
    return item[1]
sortedvals = dict(sorted(my_dict.items(), key=valuable, reverse=True))

first_two = dict(list(sortedvals.items())[:3])

print(first_two)
"""


