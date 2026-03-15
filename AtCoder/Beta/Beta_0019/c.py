import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
op = 0
i = 0
while i<n:
    j = i+1
    while j<n and arr[j]==arr[i]+1:
        j+=1
        i+=1
    i = j
    op+=1
print(op)