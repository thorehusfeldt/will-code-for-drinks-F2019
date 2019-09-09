from sys import argv
from random import randrange, shuffle


# many overlaps in order to enforce clever precomputation of p

n = int(argv[1])
f = 1
I = []
for i in range (n):
    #s = i if randrange(2) == 0 else randrange(f) # coin flip: either very long previos overlap, or random
    s = i
    I.append((s, f, randrange(1, 10**4)))
    f += 2

shuffle(I)
print (len(I))
for s, f, v in I:
    print (s, f, v)

