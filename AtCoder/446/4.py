import sys
import bisect
from collections import defaultdict
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))


d = defaultdict(int)

for x in arr:
    d[x] = d[x-1]+1

print(max(d.values()))