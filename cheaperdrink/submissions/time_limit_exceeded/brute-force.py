from itertools import permutations, combinations
from sys import stdin
import string

n = int(stdin.readline())


def flip_if_possible(s, b):
    if b and set(s) <= set('01689'):
        rev = s[::-1]
        return rev.translate(string.maketrans('69', '96'))
    else:
        return s

P =[]
for _ in range(n):
    P.append(stdin.readline().strip())

MIN = float('inf')
MINARR = None
for L in permutations(P):
    for r in range(n + 1):
        for S in combinations(range(n), r):
            arr = ''.join([ flip_if_possible(L[i], i in S) for i in range(n)])
            if int(arr) < MIN:
                MIN = int(arr)
                MINARR = arr

print MINARR
