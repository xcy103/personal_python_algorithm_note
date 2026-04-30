import sys
from collections import defaultdict
n = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().split()))

d = defaultdict(int)

for i in range(n):
    for j in range(i+1,n):
        d[arr[i]+arr[j]]+=1
print(max(d.values()))