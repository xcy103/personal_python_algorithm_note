
import sys

N,K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

t = arr[K-1]
op = 0
for x in arr:
    if x<t:
        op+=1
print(op)