import sys

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
for i,x in enumerate(arr):
    arr[i]%=k

arr = sorted(set(arr))
ans = arr[-1]-arr[0]
t = len(arr)
for i in range(t-1,0,-1):
    ans = min(ans,arr[i-1]-(arr[i]-k))
print(ans)