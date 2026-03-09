from collections import defaultdict
mat = [[9,7,8],[4,6,5],[2,8,6]]
m,n = len(mat),len(mat[0])
op = 0
d = defaultdict(int)
def check(num):
    for j in range(2,int(num**0.5) + 1):
        if num%j==0:
            return False
    return True
def f(i,j):
    #右
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][tmpj]
        if cur>10 and check(cur):
            d[cur]+=1
        tmpj+=1
    
    #右下
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][tmpj]
        if cur>10 and check(cur):
            d[cur]+=1
        tmpi+=1
        tmpj+=1
    
    #下
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][j]
        if cur>10 and check(cur):
             d[cur]+=1
        tmpi+=1
    
    #左下
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][tmpj]
        if cur>10 and check(cur):
             d[cur]+=1
        tmpi+=1
        tmpj-=1
    
    #左
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][tmpj]
        if cur>10 and check(cur):
             d[cur]+=1
        tmpi-=1
    
    #左上
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][tmpj]
        if cur>10 and check(cur):
             d[cur]+=1
        tmpi-=1
        tmpj-=1
    
    #上
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][tmpj]
        if cur>10 and check(cur):
             d[cur]+=1
        tmpi-=1
    
    #右上
    tmpi,tmpj = i,j
    cur = 0
    while tmpi<m and tmpj<n and tmpi>=0 and tmpj>=0:
        cur = cur*10 + mat[tmpi][tmpj]
        if cur>10 and check(cur):
             d[cur]+=1
        tmpi-=1
        tmpj+=1
            
            
    
for i in range(m):
    for j in range(n):
        f(i,j)
if not d:
    print(-1)
mx = max(d.values())
res = 0
for k in d.keys():
    if d[k]==mx:
        res = max(res,k)
print(-1 if res==0 else res)