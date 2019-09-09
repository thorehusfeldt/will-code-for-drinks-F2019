#!/usr/bin/python3
from itertools import combinations

n = int(input())
I = []
for _ in range(n):
    I.append(tuple(map(int, input().split())))

def valid(J):
    J.sort()
    next_idle = 0
    for s, f, _ in J:
        if s < next_idle:
            return False
        next_idle = f
    return True

MAX = 0
for r in range(1, n+1):
    for L in combinations(I, r):
        if valid(list(L)):
            MAX = max( sum([x[2] for x in L]), MAX )

print (MAX)
