import sys

k,m = map(int,sys.stdin.readline().split())
ans = list(map(int,sys.stdin.readline().split()))

print(sum(ans)%m)