import sys

n,t = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


s = 0
n = len(arr)

op = 0
for i in range(n):
    if arr[i]>=s:
        op+=arr[i] - s
        s = arr[i] + 100
        

op+=max(0,t-s)
print(op)
