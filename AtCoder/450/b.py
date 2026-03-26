import sys
n = int(sys.stdin.readline().strip())
c = []
INF = 10**10
for _ in range(n-1):
    arr = list(map(int,sys.stdin.readline().split()))
    c.append([INF]*(n-len(arr)) + arr)
c.append([INF]*n)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if c[i][k]+c[k][j]<c[i][j]:
                print('Yes')
                exit()
print('No') 