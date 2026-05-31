import sys

n,q = map(int,input().split())

res = []
for _ in range(q):
    x,y = map(int,input().split())
    x-=1
    y-=1
    if (x+y)%2==0:
        if n%2==0:
            res.append(str(n//2*x+y//2+1))
        else:
            res.append(str((n+1)//2*x-(x//2)+y//2+1))
    else:
        t = (n*n+1)//2
        if n%2==0:
            res.append(str(n//2*x+y//2+1+t))
        else:
            res.append(str((n)//2*x+(x//2)+y//2+1+t))
print('\n'.join(res))