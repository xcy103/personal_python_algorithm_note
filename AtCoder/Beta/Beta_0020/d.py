import sys
n,l = map(int ,sys.stdin.readline().split())
arr = []
for _ in range(n):
    x,r = map(int ,sys.stdin.readline().split())
    arr.append([max(0,x-r),min(x+r,l)])

arr.sort()
if arr[0][0]!=0:
    print('No')
else:
    start = arr[0][0]
    end = arr[0][1]
    i = 0
    f = 0
    while i<n and arr[i][0]<=end:
        end = max(end,arr[i][1])
        i+=1
    
    if i<n or end!=l: f = 1
    if f:
        print('No')
    else:
        print('Yes')