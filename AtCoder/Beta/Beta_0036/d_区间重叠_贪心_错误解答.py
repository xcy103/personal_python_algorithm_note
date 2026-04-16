import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    s,e = list(map(int,sys.stdin.readline().split()))
    arr.append([s,e])
arr.sort()

ans = 0
l = 0
while l<n:
    r = l
    e = arr[l][1]
    while r<n and arr[r][0]<e:
        e = min(e,arr[r][1])
        r+=1
    ans = max(ans,r-l)
    l = r
print(ans)