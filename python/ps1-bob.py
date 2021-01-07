# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
count = 0
while 'bob' in s:
    count += 1 
    s = s[(s.find('bob') + 2):]
print("Number of times bob occurs is: "+str(count))
        

