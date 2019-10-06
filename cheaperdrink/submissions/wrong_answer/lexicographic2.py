def turn(s):
    R = []
    for x in s[::-1]:
        if x in ('23457'): return s
        if x in ('018'): R.append(x)
        if x == '6': R.append('9')
        if x == '9': R.append('6')
    return min(s,''.join(R))

n = int(raw_input())
A = []
for _ in range(n):
    A.append(turn(raw_input().strip()))
A.sort()
print ''.join(A)

