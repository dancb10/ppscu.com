# There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.
"""
Example:
Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 
So you should return 1, because there is only one bulb is on.
"""

def bulb(n):
    if n == 0:
        return 0

    if n < 4:
        return 1

    total = 1
    diff = 5
    curr = 4
    while curr <= n:
        total += 1
        curr += diff
        diff += 2
    return total

print(bulb(10))
