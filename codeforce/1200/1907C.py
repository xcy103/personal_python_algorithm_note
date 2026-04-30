import sys
from collections import Counter
t = int(sys.stdin.readline().strip())

res = []
for _ in range(t):
    _ = int(sys.stdin.readline().strip())
    s = list(sys.stdin.readline().split()[0])
    c = Counter(s)
    mx = max(c.values())
    n = len(s)
    res.append(str(n-(min(n//2,n-mx)*2)))

sys.stdout.write('\n'.join(res))
