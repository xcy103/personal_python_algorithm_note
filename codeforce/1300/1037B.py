import sys

n,s = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = 0

if arr[n//2]<=s:
    for i in range(n//2,n):
        ans+=max(s-arr[i],0)
else:
    for i in range(n//2,-1,-1):
        ans+=max(arr[i]-s,0)

print(ans)