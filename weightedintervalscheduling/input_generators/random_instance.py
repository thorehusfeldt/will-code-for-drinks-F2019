from random import randrange
from sys import argv
MAX = 10**9
n = int(argv[1])
assert (1 <= n <= 10**5)
print (n)
for _ in range(n):
    s = randrange(MAX + 1)
    t = randrange(MAX + 1)
    v = randrange(1, 10**4)
    while s == t:
        t = randrange(MAX + 1)
    start = min(s,t)
    finish = max(s,t)
    print (start, finish, v)
