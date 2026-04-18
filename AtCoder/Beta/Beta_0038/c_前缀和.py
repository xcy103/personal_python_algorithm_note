import sys

n,l,k = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
p = 0
i = 0
while i<n and i<=k:
    p+=arr[i]
    if p>l:
        break
    i+=1
print(i)