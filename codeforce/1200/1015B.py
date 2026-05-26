import sys
from collections import Counter
n = int(input())
s = list(input().split()[0])
t = list(input().split()[0])

res = []
#就是暴力
tmps = s[:]
tmps.sort()
tmpt = t[:]
tmpt.sort()
if tmpt!=tmps:
    print(-1)
    exit(0)
idx = n-1
while idx:
    if s[idx]!=t[idx]:
        #开始搜索s
        tmp = idx
        while tmp:
            if s[tmp]==t[idx]:
                break
            tmp-=1
        #找到了相等的，开始交换
        for k in range(tmp,idx):
            res.append(k+1)
            s[k],s[k+1] = s[k+1],s[k]
    idx-=1
print(len(res))
if res:print(*res)