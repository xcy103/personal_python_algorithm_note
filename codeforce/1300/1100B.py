import sys
from collections import defaultdict
m,n = map(int,input().split())
arr = list(map(int,input().split()))

d = defaultdict(int)
res = []
cnt = [0]*(m+1)
k = 1
for x in arr:
    cnt[x]+=1
    d[cnt[x]]+=1
    if d[k]==m:
        k+=1
        res.append('1')
    else:
        res.append('0')    
print(''.join(res))