import sys

n,k = list(map(int,sys.stdin.readline().split()))
A = list(map(int,sys.stdin.readline().split()))
B=  list(map(int,sys.stdin.readline().split()))

l = r = 0
sb = 0
sa = 0
ans = 0
while r<n:
    sb+=B[r]
    sa+=A[r]
    while sb>k:
        sb-=B[l]
        sa-=A[l]
        l+=1
    r+=1
    ans = max(ans,sa)
print(ans)