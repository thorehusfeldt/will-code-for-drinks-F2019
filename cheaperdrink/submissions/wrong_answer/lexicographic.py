n = int(raw_input())
A = []
for _ in range(n):
    A.append(raw_input().strip())
A.sort()
print ''.join(A)

