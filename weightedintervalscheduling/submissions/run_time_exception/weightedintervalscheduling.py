#!/usr/bin/python3
# Segmentation fault on my machine
import bisect
import sys
sys.setrecursionlimit(10**5)
n = int(input())
assert 0 <= n <= 10**5
I = [tuple(map (int, input().split())) for _ in range(n)]
I.sort(key = lambda t: t[1])

p = [None] * n # p[j] = index of highest-indexed interval still fitting before I[j] (None otherwise)
F = [t[1] for t in I]
for i in range(n):
    s = I[i][0]
    p[i] = bisect.bisect_right(F, s) - 1

def OPT(j):
    ''' opt of first j intervals 0,..., j-1 '''
    global p, M
    print (j)
    if M[j] is not None:
        return M[j]
    if p[j - 1] is not None:
        M[j] = max (I[j-1][2] + OPT(p[j - 1] + 1), OPT(j-1))
    else:
        M[j] = max (I[j-1][2] , OPT(j-1))
    assert 1 <= M[j] <= 10**9
    return M[j]

M = [0] + [None] * n 
print (OPT(n))
