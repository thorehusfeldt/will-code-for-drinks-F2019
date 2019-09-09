# the answer uses ~ 50000 intervals and is billions large
from random import randrange, sample, shuffle
from sys import argv
n = int(argv[1])
MAX = 10**9 

def spread_intervals():
    # partition the total weight and the interval boundaries equally across MAX
    weights = [0]
    #weights.extend(sorted(sample(range(1, MAX // 2), n//2)))
    weights.extend(sorted(sample(range(1, MAX), n)))
    starts = [0]
    #starts.extend(sorted(sample(range(1, MAX + 1), n//2)))
    starts.extend(sorted(sample(range(1, MAX + 1), n)))
    I = []
    #for i in range(n//2):
    for i in range(n):
        s, f = starts[i], starts[i+1]
        w = weights[i+1] - weights[i]
        I.append((s,f,w))
    return I

J = spread_intervals() 
#J.extend(spread_intervals()) # do it again, just to get some overlaps
shuffle(J)
print (len(J))
for s, f, w in J:
    print (s, f, w)



