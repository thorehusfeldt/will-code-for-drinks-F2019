#!/usr/bin/env python3

def turn(s):
    R = []
    for x in s[::-1]:
        if x in ('23457'): return s
        if x in ('018'): R.append(x)
        if x == '6': R.append('9')
        if x == '9': R.append('6')
    return min(s,''.join(R))

class K:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        return self.s + other.s < other.s + self.s

n = int(input())
A = []
for _ in range(n):
    A.append(K(turn(input())))
A.sort()
print(''.join(x.s for x in A))
