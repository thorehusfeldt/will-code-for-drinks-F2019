from __future__ import print_function 
from sys import stdin

def non_overlapping(I):
    idle = 0
    for s, f in I:
        if s >= idle:
            yield s, f
            idle = f

n = int(stdin.readline())
I = []
for i in range(0, n):
    s, f = stdin.readline().split()
    I.append((int(s), int(f)))
I.sort(key = lambda t: t[-1])

print (len(list(non_overlapping(I))))
