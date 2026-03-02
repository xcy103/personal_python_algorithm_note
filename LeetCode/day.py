g = [[1,0,0],[1,1,0],[1,1,1]]
n = len(g)
ans = [0]*n
for i in range(n):
    t = 0
    for j in range(n):
        if g[i][j] == 1:
            t = 0
        else:
            t+=1
    ans[i] = t
tmp = ans[:]
tmp.sort()
tmp.reverse()
for i in range(n):
    if tmp[i]<n-i-1:print -1
op = 0
t = 0
for target in range(n-1,-1,-1):
    i = t
    while i<n:
        if ans[i]>=target:
            break
        i+=1
    tmp = ans[:]
    for j in range(i,t,-1):
        tmp[j],tmp[j-1]=tmp[j-1],tmp[j]
    op+=i-t
    t+=1
    ans = tmp[:]
print(op)