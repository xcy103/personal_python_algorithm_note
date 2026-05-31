import sys
from collections import defaultdict
n,q = map(int,input().split())
t = 0
#t就是刚开始的基准线
#1 x,在x处添加砖块，如果全部都>=1，每个减去1个
#2 y,查询所有至少有y个砖块的cell个数

d = defaultdict(int)
arr = [0]*(n+1)
s = 0
res = []
for _ in range(q):
    op,coor = map(int,input().split())
    if op==1:
        arr[coor]+=1
        d[arr[coor]]+=1
        if d[arr[coor]]==n:
            t+=1
    else:
        res.append(str(d[coor+t]))
print('\n'.join(res))