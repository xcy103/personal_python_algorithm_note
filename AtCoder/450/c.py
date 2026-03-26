import sys
sys.setrecursionlimit(10**7)
h,w = map(int,sys.stdin.readline().split())
g = []
for _ in range(h):
    g.append(list(sys.stdin.readline().strip()))

def f(i,j):
    if i<0 or j<0 or i==h or j==w or g[i][j]=='#':
        return 
    g[i][j] = '#'
    f(i-1,j)
    f(i+1,j)
    f(i,j-1)
    f(i,j+1)

for i in range(h):
    if g[i][0]=='.':
        f(i,0)
    if g[i][w-1]=='.':
        f(i,w-1)
for j in range(w):
    if g[0][j]=='.':
        f(0,j)
    if g[h-1][j]=='.':
        f(h-1,j)

op = 0
for i in range(h):
    for j in range(w):
        if g[i][j]=='.':
            op+=1
            f(i,j)
print(op)
        
