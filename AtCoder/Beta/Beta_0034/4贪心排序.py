import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key= lambda x:x[1])

l = 0
op = 0
while l<n:
    e = arr[l][1]
    while l<n and arr[l][0]<e:
        l+=1
    op+=1
print(op) 