import sys

n,k = map(int,input().split())
arr = list(map(int,input().split()))
if k==1:
    print(max(arr))
    print(n)
    exit(0)
nums = [(x,i) for i,x in enumerate(arr)]
nums.sort(reverse=True)
tmp = nums[:k]
op = 0
res = []
idx = [-1]
for i in range(k):
    op+=tmp[i][0]
    idx.append(tmp[i][1])

idx.sort()
idx[-1] = n-1
for i in range(1,len(idx)):
    res.append(idx[i]-idx[i-1])
print(op)
print(*res)




    
