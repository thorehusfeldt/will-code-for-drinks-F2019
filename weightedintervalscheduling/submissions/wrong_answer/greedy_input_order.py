#!/usr/bin/python3
I = [tuple(map (int, input().split())) for _ in range(int(input()))]
next_idle = 0
res = 0
for start, finish, weight in I:
    if start >= next_idle:
        res += weight
        next_idle = finish
print (res)
