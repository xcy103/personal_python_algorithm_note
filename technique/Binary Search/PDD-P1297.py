import sys

n,m,a,b = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
l = 0
r = 10**12

def check(feed):
    global n,m,a,b
    op = 0
    for x in arr:
        op+=max(0,(m-(x+b*feed)) + a-b-1//(a-b))
    
    return op<=feed
    
while l+1<r:
    mid = (l+r)//2
    if check(mid):
        r = mid
    else:
        l = mid
print(r)