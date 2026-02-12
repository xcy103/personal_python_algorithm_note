p = [[0,0],[0,2],[2,0],[2,2],[3,3]]
n = len(p)

p.sort()
res = []
ans = -1
for i in range(n-3):
    x1,y1 = p[i][0],p[i][1]
    for j in range(i+1,n-2):
        x2,y2 = p[j][0],p[j][1]
        if x1!=x2:continue
        for k in range(j+1,n-1):
            x3,y3 = p[k][0],p[k][1]
            for m in range(k+1,n):
                x4,y4 = p[m][0],p[m][1]
            if x3!=x4:continue
            if y1==y3 and y2==y4:
                res.append([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
for [x1,y1],[x2,y2],[x3,y3],[x4,y4] in res:
    f = 1
    for x,y in p:
        if (x,y) not in((x1,y1),(x2,y2),(x3,y3),(x4,y4)):
            if (x>=x1 and x<=x3) and (y>=y1 and y<=y2):
                f = 0
                break
    if f: ans = max((x3-x1)*(y2-y1),ans)
