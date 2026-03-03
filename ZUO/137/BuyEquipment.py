import sys

input = sys.stdin.readline

MAXN = 502
MAXM = 502
sml = 1e-5

n,m = map(int,input().split())

mat = [[0.0]*(m+2) for _ in range(n+1)]

for i in range(1,n+1):
    arr = list(map(int,input().split()))
    for j in range(1,m+1):
        mat[i][j] = arr[j-1]

prices = list(map(int,input().split()))
for i in range(1,n+1):
    mat[i][m+1] = prices[i-1]


basis = [0]*(m+1)

def insert(i):
    for j in range(1,m+1):
        if abs(mat[i][j])>=sml:
            if basis[j] == 0:
                basis[j] = i
                return True
            rate = mat[i][j]/mat[basis[j]][j]
            for k in range(j,m+1):
                mat[i][k]-=rate*mat[basis[j]][k]
    return False

items = list(range(1, n + 1))
items.sort(key=lambda i: mat[i][m + 1])
cnt = 0
cost = 0
for idx in items:
    if insert(idx):
        cnt+=1
        cost+=mat[idx][m+1]

print(cnt,cost)