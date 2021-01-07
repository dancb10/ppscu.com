# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:14:32 2017

@author: dan.popescu
"""

epsilon = 0.01
y = 24.0
guess = y/2.0
num = 0

while abs(guess*guess -y) >= epsilon:
    num += 1
    guess = guess - (((guess**2) -y )/(2*guess))
print('num = '+str(num))
print('square ' +str(y) + ' is ' +str(guess))
