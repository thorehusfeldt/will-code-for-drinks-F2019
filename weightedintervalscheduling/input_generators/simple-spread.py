# 99999 tiny intervals spread out over the entire range, summing to 10^9
# one big interval covers all of them, slightly larger or smaller
from random import randrange, shuffle
import sys

n = 100000 
I = []
for i in range(n - 1):
    I.append ((1000 * i  + randrange(100) , 1000 * i + randrange(500, 1000), randrange(1, 1000)))

s = sum([t[2] for t in I])
sys.stderr.write(str(s) + '\n')
# I.append((0, 10**9, s - 1))
I.append((0, 10**9, s + 1))
shuffle(I)
print (len(I))
for s, f, w in I:
    print(s,f,w)


