from __future__ import division
from sys import stdin, stdout
from bisect import bisect_left

def countInversions(L):
    if len(L) <= 1:
        return L, 0
    mid = len(L)//2
    A, a = countInversions(L[:mid])
    B, b = countInversions(L[mid:])
    return sorted(A + B), a + b + sum([bisect_left(B, x/2) for x in A])

stdin.readline()
L = list(map(int, stdin.readline().split()))
stdout.write(str(countInversions(L)[1]) + '\n')
