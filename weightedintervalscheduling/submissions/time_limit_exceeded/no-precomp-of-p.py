#!/usr/bin/python3
# Correct DP, but spends linear time each round to determine relevant previous entry
# Quadratic total time

n = int(input())
I = [tuple(map (int, input().split())) for _ in range(n)]
for s, f, v in I:
    assert (0 <= s < f <= 10**9)
    assert (1 <= v <= 10**9)
I.sort(key = lambda t: t[1]) # sort by finish time, earliest first

M = [0]
for j in range(1, n + 1):
    v = I[j-1][2]
    s = I[j-1][0]
    prev = j - 2
    while (prev >= 0 and I[prev][1] > s):
        prev -= 1
    smaller = M[prev + 1] if prev >= 0 else 0
    M.append(max (v + smaller, M[j-1]))

assert (1 <= M[n] <= 10**9)
print (M[n])
