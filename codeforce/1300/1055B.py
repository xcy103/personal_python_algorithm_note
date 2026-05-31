import sys

n,m,l = map(int,input().split())
arr = list(map(int,input().split()))
#并查集。。
idx = []
for _ in range(m):
    ops = list(map(int,input().split()))
    if ops[0]==1:
        arr[ops[1]-1]+=ops[2]
    idx.append(ops)

res = []
init = 0
i = 0
while i<n:
    j = i
    while j<n and arr[j]>l:
        j+=1
    if j>=i+1:
        init+=1
    i = max(i+1,j)

for ops in idx[::-1]:
    if ops[0]==1:
        i = ops[1]-1
        x = ops[2]
        old = arr[i]
        arr[i]-=x
        if arr[i]<=l and old>l:
            p1 = 0
            p2 = 0
            if i-1>=0 and arr[i-1]>l:
                p1 = 1
            if i+1<n and arr[i+1]>l:
                p2 = 1
            if p1 and p2:
                init+=1
            elif p1 or p2:
                init-=0
            else:
                if old>l:
                    init-=1
            
    else:
        res.append(str(init))
print('\n'.join(res[::-1]))
