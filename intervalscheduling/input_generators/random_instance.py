from random import randrange
from sys import argv
MAX = 10**9
n = int(argv[1])
print (n)
for _ in range(n):
    s = randrange(MAX)
    t = randrange(MAX)
    while s == t:
        t = randrange(MAX)
    start = min(s,t)
    finish = max(s,t)
    print (start, finish)
