#!/usr/bin/python3
import bisect
n = int(input())
I = [tuple(map (int, input().split())) for _ in range(n)]
for s, f, v in I:
    assert (0 <= s < f <= 10**9)
    assert (1 <= v <= 10**9)
I.sort(key = lambda t: t[1]) # sort by finish time, earliest first


p = [None] * n # p[j] = highest index of interval still fitting before I[j] (None otherwise)
F = [t[1] for t in I]
for i in range(n):
    s = I[i][0]
    p[i] = bisect.bisect_right(F, s) - 1

M = [0]
for j in range(1, n + 1):
    M.append(max(I[j-1][2] + (M[p[j-1] +1] if p[j-1] is not None else 0), M[j-1]))

assert (1 <= M[n] <= 10**9)
print (M[n])
