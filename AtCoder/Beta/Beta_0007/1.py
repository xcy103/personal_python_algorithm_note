import sys

n,m = map(int,sys.stdin.readline().split())
e = list(map(int,sys.stdin.readline().split()))
c = list(map(int,sys.stdin.readline().split()))

t = min(e)
print(sum(c)*t)