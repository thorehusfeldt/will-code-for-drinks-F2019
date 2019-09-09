#!/usr/bin/python3
import bisect
from sys import stdin
n = int(input())
I = []
for line in stdin:
    s, f, w = map(int, line.split())
    I.append((f,s,w)) # finish time first, to make sorting easier

I.sort() 
F = [f for f, _, _ in I] # finish times (for the binary search below)
M = [0]
for _, s, w in I:
    prev = bisect.bisect_right(F, s)
    take = w + (M[prev] if prev else 0)
    drop = M[-1]
    M.append( max(take, drop) )

assert (1 <= M[-1] <= 10**9)
print (M[-1])
