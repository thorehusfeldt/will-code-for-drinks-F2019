from util import *

n = int(cmdlinearg('n'))
first = cmdlinearg('first')
second = cmdlinearg('second')

n1 = n//2
n2 = n - n1

s1 = list(range(     1,      n1 + 1))
s2 = list(range(n1 + 1, n1 + n2 + 1))
if first == 'down':
    s1.reverse()
if second == 'down':
    s2.reverse()
print(n)
print (' '.join(map(str, s1 + s2 )))

