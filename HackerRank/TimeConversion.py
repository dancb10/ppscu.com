'''
Given a time in -hour AM/PM format, convert it to military (-hour) time.

Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.

Input Format

A single string containing a time in -hour clock format (i.e.:  or ), where  and .

Output Format

Convert and print the given time in -hour format, where .

Sample Input

07:05:45PM
Sample Output

19:05:45
'''

#!/bin/python

import sys
from datetime import *

def timeConversion(s):
    datep = datetime.strptime(s,'%I:%M:%S%p')
    tc = datep.strftime('%H:%M:%S')
    return tc

s = raw_input().strip()
result = timeConversion(s)
print(result)
