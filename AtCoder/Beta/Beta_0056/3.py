import sys


n,k = map(int,input().split())
arr = list(map(int,input().split()))

l = 0
s = 0
ans = 0
for r in range(n):
    s+=arr[r]
    while s>k:
        s-=arr[l]
        l+=1
    ans = max(r-l+1,ans)
print(ans)