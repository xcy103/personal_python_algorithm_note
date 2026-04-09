import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()
print(arr[-1]+arr[-2])