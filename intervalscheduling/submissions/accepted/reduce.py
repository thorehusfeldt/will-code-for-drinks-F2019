from __future__ import print_function 
from functools import reduce
from sys import stdin
n = int(stdin.readline())
I = []
for i in range(0, n):
    s, f = stdin.readline().split()
    I.append((int(s), int(f)))
I.sort(key = lambda t: t[-1])
ct = 0
def no_overlap(i1, i2):
    global ct
    if i2[0] < i1[1]:
        return i1 
    else:
        ct += 1
        return i2
reduce(no_overlap, I)
print (ct + 1)

