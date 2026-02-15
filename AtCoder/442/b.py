import sys

data = sys.stdin.read().split()
ptr = 0
n,m = map(int, data[ptr:ptr+2])
ptr += 2
cnt = [n]*(n+1)

for _ in  range(m):
    p1,p2 = map(int, data[ptr:ptr+2])
    ptr+=2
    cnt[p1] -= 1
    cnt[p2] += 1

ans = [0]*(n+1)
for i in range(1,n+1):
    if cnt[i]<=3:
        ans[i] = 0
    else:
        ans[i] = (cnt[i]-1)*(cnt[i]-2)//2

print(*ans[1:])