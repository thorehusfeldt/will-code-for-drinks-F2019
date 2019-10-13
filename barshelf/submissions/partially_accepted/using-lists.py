from sys import stdin
from bisect import bisect_left, bisect_right, insort
n = int(stdin.readline())
H = list(map(int, stdin.readline().split()))
smaller = [0] * n
larger  = [0] * n
left, right = [], []

for i in range(n):
    larger[i] = len(left) - bisect_left(left, H[i] * 2)
    insort(left, H[i])

for i in reversed(range(n)):
    smaller[i] = bisect_right(right, H[i] / 2)
    insort(right, H[i])

print (sum([larger[i] * smaller[i] for i in range(n)]))
