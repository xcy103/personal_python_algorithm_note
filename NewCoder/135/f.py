#贡献法
import sys
from collections import defaultdict 
t = int(input())

mod = 998244353
res = []

def ksm(a,p,mod):
    ans = 1
    while p:
        if p&1: ans = (ans * a)%mod
        p>>=1
        a = (a*a)%mod
    return ans

for _ in range(t):
    n,m,k = list(map(int,input().split()))
    dx = defaultdict(int)
    dy = defaultdict(int)
    nodes = []
    for _ in range(k):
        x,y = list(map(int,input().split()))
        dx[x]+=1
        dy[y]+=1
        nodes.append((x,y))
    
    #开始算贡献
    ans = 0
    #在预设的点里
    for x,y in nodes:
        if dx[x]==1 and dy[y]==1:
            ans = (ans + ksm(2,(n*m-n-m+1-(k-1))%(mod-1) + (mod-1),mod))%mod
    
    
    S = (n-len(dx))*(m-len(dy))%mod
    if k<n*m:
        ans = (ans + S*ksm(2,(n*m-n-m+1-k)%(mod-1) + (mod-1),mod))%mod
    
    res.append(str(ans))

print('\n'.join(res))
    
