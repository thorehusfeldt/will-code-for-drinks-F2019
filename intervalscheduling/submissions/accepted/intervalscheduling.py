#!/usr/bin/python
from __future__ import print_function 
from sys import stdin
n = int(stdin.readline())
I = []
for i in range(0, n):
    s, f = stdin.readline().split()
    I.append((int(s), int(f)))
I.sort(key = lambda t: t[-1])
next_idle = 0
res = 0
for start, finish in I:
    if start >= next_idle:
        res += 1
        next_idle = finish
print (res)

