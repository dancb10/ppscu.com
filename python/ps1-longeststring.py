# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc 
"""

s = 'azcbobobegghakl'
count = 0
while 'bob' in s:
    count += 1 
    s = s[(s.find('bob') + 2):]
print("Number of times bob occurs is: "+str(count))
        

