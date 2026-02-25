import sys
N,T,C,D = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

op = 0
for x in arr:
    if x>=T:
        op+=1

print(min(C,D)*op)