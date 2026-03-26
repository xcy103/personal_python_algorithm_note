import sys


n,s,q = map(int,sys.stdin.readline().split())
x_coor = list(map(int,sys.stdin.readline().split()))

t = []
for i in range(n):
    t.append((x_coor[i],i+1))
t.sort()
pos = [0]*(n+1)
for i in range(n):
    pos[t[i][1]] = i

MAXP = 62
stjump = [[0]*MAXP for _ in range(n)]
for i in range(n):
    if i==0:
        stjump[0][0] = 1
    elif i==n-1:
        stjump[n-1][0] = n-2
    else:
        pre = t[i][0] - t[i-1][0]
        suf = t[i+1][0] - t[i][0]
        if pre<suf:
            stjump[i][0] = i-1
        elif pre>suf:
            stjump[i][0] = i+1
        else:
            if t[i-1][1]<t[i+1][1]:
                stjump[i][0] = i-1
            else:
                stjump[i][0] = i+1
for k in range(1,MAXP):
    for i in range(n):
        stjump[i][k] = stjump[stjump[i][k-1]][k-1]
#倍增表构造好了，，不太知道该怎么搞了
cur = pos[s]
for k in range(MAXP):
    if (q>>k)&1:
        cur = stjump[cur][k]
print(t[cur][1])

