import sys

n,a,k = map(int,input().split())

t = a//n
res = [t]*n
left = a%n
if len(res)%2==0:
    l = len(res)-1
    for i in range(left):
        res[l]+=1
        l-=1
else:
    left = (a%n) + res[-1]-1
    res[-1] = 1
    res[0]+=left//2
    res[1]+=left//2
    if left%2:
        res[-1]+=1
    


op = 0
tmp = res[:]
for i in range(1,len(res)):
    op+=tmp[i-1]
    tmp[i]-=tmp[i-1]
if tmp[-1]:
    op+=tmp[-1]
if op!=k:
    print(-1)
else:
    print(*res)