n = int(raw_input())
A = []
for _ in range(n):
    A.append(int(raw_input()))
A.sort()
print ''.join([str(a) for a in A])

