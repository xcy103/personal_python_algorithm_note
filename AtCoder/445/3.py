import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int,sys.stdin.readline().split()))
arr = [0]+arr


t = 1
c = []
ans = [0]*(n+1)
for i in range(1,n+1):
    if ans[i]:continue
    j = i
    vis = [0]*(n+1)
    tmp = []
    while vis[j]==0:
        tmp.append(j)
        vis[j] = t
        t+=1
        j = arr[j]
    if t-vis[j]==1:
        for x in tmp:
            ans[x] = str(j)
    else:
        l = t-vis[j]
        for x in tmp:
            # k = x
            step = pow(10,100,l)
            # while step:
            #     k = arr[k]
            #     step-=1
            ans[x] = str(tmp[(x+step)%l])

print(' '.join(ans[1:])+'\n')  


