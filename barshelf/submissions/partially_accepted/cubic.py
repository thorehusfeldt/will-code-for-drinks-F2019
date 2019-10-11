#!/usr/bin/python3
input()
L = list(map(int, input().split()))
count = 0
for i in range(len(L) - 2):
    for j in range(i + 1, len(L) - 1):
        for k in range(j + 1, len(L)):
            if L[i] >= 2 * L[j] >= 4 * L[k]:
                count += 1

print (count)
