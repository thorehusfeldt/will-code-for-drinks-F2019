#!/usr/bin/python3
I = [tuple(map (int, input().split())) for _ in range(int(input()))]
I.sort(key = lambda t: t[2] / (t[1] - t[0]), reverse = True)
next_idle = 0
res = 0
for start, finish, weight in I:
    if start >= next_idle:
        res += weight
        next_idle = finish
print (res)


