# 注意是左还是右中位数
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
mid = (n+1)//2 - 1

l = mid
r = mid
while l>=0 and arr[l]==arr[mid]:
    l-=1
while r<n and arr[r]==arr[mid]:
    r+=1
if l<0 and r>=n:
    print(-1)
    exit()

ans = 10**18
if l>=0:
    ans = min(ans,n-2*(l+1))
if r<n:
    ans = min(ans,n-2*(n-r)+1)
print(ans if ans!=10**18 else -1)