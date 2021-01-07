# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:14:32 2017

@author: dan.popescu
"""

x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Reminder = ' + str((2**p)*x - int((2**p)*x)) )
    p += 1

num = int(x*(2**p))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]

print('The binary representation of teh decimal ' +str(x)+' is '+ str(result))    
        


