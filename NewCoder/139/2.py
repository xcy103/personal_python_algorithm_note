import sys

n,m = list(map(int,sys.stdin.readline().split()))
if n>1 and m>1:
    print('-1')
    exit(0)
res = [[None]*m for _ in range(n)]
res[0][0] = '1'
for i in range(n):
    for j in range(m):
        if i==0 and j==0:continue
        res[i][j] = '0'
print('\n'.join([''.join(x) for x in res]))

