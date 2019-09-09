#!/usr/bin/python3
n = int(input())
I = [tuple(map (int, input().split())) for _ in range(n)]
I.sort(key = lambda t: t[1])

p = [None] * n # p[j] = index of highest-indexed interval still fitting before I[j] (None otherwise)
for i in range(n):
    s = I[i][0]
    p[i] = None
    for j in range(i):
        if I[j][1] <= s:
            p[i] = j

def OPT(j):
    ''' opt of first j intervals 0,..., j-1 '''
    global p, M
    if M[j] is not None:
        return M[j]
    if p[j - 1] is not None:
        M[j] = max (I[j-1][2] + OPT(p[j - 1] + 1), OPT(j-1))
    else:
        M[j] = max (I[j-1][2] , OPT(j-1))
    return M[j]

M = [0] + [None] * n 
print (OPT(n))
