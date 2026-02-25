import sys
n,m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(m):
    l,r = map(int, sys.stdin.readline().split())
    arr.append([l,r])

arr.sort()
op = 0
j = 0
nums = []
while j<m:
    l,r = arr[j][0],arr[j][1]
    e = r
    while j<m and arr[j][0]<=e:
        e = max(e,arr[j][1])
        j+=1
    if l>op+n:break
    op+=e-l+1

print(n+op)