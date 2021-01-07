# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:14:32 2017

@author: dan.popescu
"""

number=int(input('Enter a number to be converted to binary:'))
result=''
isnegative=''

if number < 0:
    isnegative='True'
    number=abs(number)
elif number > 0:
    isnegative='False'
elif number == 0:
    result += '0'    
while number > 0:    
    result=str(number%2)+result
    number=number//2
if isnegative == 'True':
    print('Answer is: -'+result)
else:
    print('Answer is: '+result)