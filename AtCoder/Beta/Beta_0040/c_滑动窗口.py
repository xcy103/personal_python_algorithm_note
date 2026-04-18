import sys

n,k = list(map(int,sys.stdin.readline().split()))
pos = list(map(int,sys.stdin.readline().split()))
pos.sort()
ans = 0
l = r = 0
while r<n:
    while pos[r]-pos[l]>k:
        l+=1
    ans = max(r-l+1,ans)
    r+=1
print(ans)