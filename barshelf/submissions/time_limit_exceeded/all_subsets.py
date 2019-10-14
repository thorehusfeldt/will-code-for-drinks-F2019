#!/usr/bin/python3
# TLE: iterate over all subsets, check if this subset has size three,
# extract the corresponding trio, and see if it is messy
n = int(input())
H = list(map(int, input().split()))

ct = 0
for i in range(2**n):
    bitrep = format(i, '0'+str(n)+'b') # to bit representation with leading 0s
    numbits = sum(map(int, bitrep))
    if numbits == 3:
        trio = ([H[id] for  id, b in enumerate(bitrep) if b == '1'])
        if trio[0] >= 2 * trio[1] >= 4 * trio[2]:
            #print (trio)
            ct += 1

print (ct)
