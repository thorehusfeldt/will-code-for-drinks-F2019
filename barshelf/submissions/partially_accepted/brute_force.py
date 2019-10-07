#!/usr/bin/python3
input()
L = list(map(int, input().split()))
count = 0
for i in range(len(L) -1):
    for j in range(i + 1, len(L)):
        if L[i] > 2 * L[j]:
            count += 1

print (count)
