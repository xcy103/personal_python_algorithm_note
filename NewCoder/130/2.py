import sys


t = int(input())

res = []
for _ in range(t):
    n = int(input())

    g = []
    for _ in range(n):
        g.append(list(input().strip()))
    ix = []
    iy = []
    for i in range(n):
        for j in range(n):
            if g[i][j]=='*':
                ix.append(i)
                iy.append(j)
    
    if len(set(ix))==2:
        iy.sort()
        if iy[1]==iy[2]:
            res.append('T')
        else:
            res.append('L')
    else:
        ix.sort()
        if ix[1]==ix[2]:
            res.append('T')
        else:
            res.append('L')

print('\n'.join(res))
    
    
