from util import *

n = int(cmdlinearg('n'))

increment = 10**9 // n
bottles = reversed(range(1, n * increment, increment))
print (n)
print (' '.join(map(str, bottles)))
