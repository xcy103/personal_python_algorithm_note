g = [[7,9,8]]
m,n = len(g),len(g[0])
ans = 0
for k in range(3,-1,-1):
    t = 1
    for i in range(m):
        f = 0
        for j in range(n):
            if (g[i][j])|(ans)<=ans:
                f = 1
                break
        if f==0:
            t = 0
    if t==0:
        ans|=1<<k
print( ans)