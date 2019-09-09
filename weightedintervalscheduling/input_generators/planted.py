#!/usr/bin/python3
import bisect
from random import randrange, sample, shuffle
def solve(intervals):
    intervals.sort(key = lambda t: t[1])
    p = [None] * len(intervals) # p[j] = highest index of interval still fitting before I[j] (None otherwise)
    F = [t[1] for t in intervals]
    for i in range(len(intervals)):
        s = intervals[i][0]
        p[i] = bisect.bisect_right(F, s) - 1

    DP = [0]
    for j in range(1, len(intervals) + 1):
        DP.append(max(intervals[j-1][2] + (DP[p[j-1] +1] if p[j-1] >= 0 else 0), DP[j-1]))
    return (DP[-1])

n = 90000

# start with a random instance in [0, MAX] of 9*10^5 intervals
# the length is 10^1 to 10^5, uniformly by # digits
# weight is random in [1,10^4]
#MAX = 10**6
MAX = 10**9


I = []
for _ in range(n):
    digits = randrange(1, 6)
    l = randrange(1, 10**digits)
    s = randrange(MAX - l)
    v = randrange(1, 10**4)
    I.append( (s, s + l, v) )

oldval = solve(I)
assert (10000 <= oldval <= 10**9)
newval = oldval + 1

# add ten thousand tiny intervals that fit and sum to newval, tightly

bits = [0]
bits.extend( sample(range(1, newval), 9999))
bits.append(newval)
bits.sort()

starts = sample(range(0,MAX,2), 10001)
starts.sort()
J = []
for i in range(10000):
    J.append (( starts[i], starts[i + 1] - 1, bits[i+1]-bits[i]))
assert (newval == sum([t[2] for t in J]))

I.extend(J)
sol = solve(I)
assert (oldval < sol <= 10**9)
shuffle(I)
print (len(I))
for s, f, v in I:
    print (s, f, v)

