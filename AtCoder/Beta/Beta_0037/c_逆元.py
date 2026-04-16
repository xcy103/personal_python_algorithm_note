import sys

n,k = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

mod = 10**9+7
l = 0
r = 0
s = 1
ans = 0
inv = [0]*n
for i in range(n):
    inv[i] = pow(arr[i],mod-2,mod)
for _ in range(k-1):
    s = s*arr[r]%mod
    r+=1
while r<n:
    s = s*arr[r]%mod
    ans = (ans + s)%mod
    s*=inv[l]
    l+=1
    r+=1
print(ans)