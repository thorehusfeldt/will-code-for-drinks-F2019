#!/usr/bin/python3
from itertools import combinations

n = int(input())
I = []
for _ in range(n):
    line = input().split()
    s, f = int(line[0]), int(line[1])
    I.append((s,f))

def valid(J):
    J.sort()
    next_idle = 0
    for s, f in J:
        if s < next_idle:
            return False
        next_idle = f
    return True

for r in range(n, 0, -1):
    for L in combinations(I, r):
        if valid(list(L)):
            print(r)
            exit(0)

assert (False) # singleton solution must work

