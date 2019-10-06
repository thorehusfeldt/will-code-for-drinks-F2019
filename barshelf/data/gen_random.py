from util import *
from random import randrange

n = int(cmdlinearg('n'))

print(n)
print (' '.join([str(randrange(10**9)) for _ in range(n)]))
