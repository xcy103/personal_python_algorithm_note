import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
if m>=n:
    print(0)
else:
    print(arr[n-m-1])