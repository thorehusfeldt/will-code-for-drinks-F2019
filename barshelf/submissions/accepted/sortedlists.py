import sys
from bisect import bisect, insort

lists = []
buf = []
ans = 0
sys.stdin.readline()
for b in map(int,sys.stdin.read().split()):
    ans += len(buf) - bisect(buf, b << 1)
    for l in lists:
        ans += len(l) - bisect(l, b << 1)
    if len(buf) == 10000:
        lists.append(buf)
        buf = [b]
    else:
        insort(buf, b)
print(ans)
