#!/usr/bin/python
I = [tuple(map (int, raw_input().split())) for _ in range(int(raw_input()))]
I.sort(key = lambda t: t[1])
next_idle = 0
res = 0
for start, finish in I:
    if start >= next_idle:
        res += 1
        next_idle = finish
print res

