#其实是算贡献，之前的做法是划分DP，是不对的

t = int(input())
mod = 998244353

res = []
for _ in range(t):
    n = int(input())
    s = input()
    is_pa = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pa[i][i] = True
        if i + 1 < n:
            is_pa[i][i + 1] = (s[i] == s[i + 1])
    for i in range(n - 3,-1,-1):
        for j in range(i + 2,n):
            if s[i] == s[j]:
                is_pa[i][j] = is_pa[i + 1][j - 1]
    
    pre = [0]*n
    suf = [0]*n
    for i in range(n):
        for j in range(i,-1,-1):
            if is_pa[j][i]:
                pre[i] = (pre[i] + (pre[j-1] if j>0 else 1))%mod
    
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if is_pa[i][j]:
                suf[i] = (suf[i] + (suf[j+1] if j+1<n else 1))%mod
    
            
    ans = 0
    for i in range(n):
        for j in range(i,n):
            if is_pa[i][j]:
                ans = (ans + (pre[i-1] if i>0 else 1)*
                       (suf[j+1] if j+1<n else 1)*(j-i+1)*(j-i+1))%mod
    res.append(str(ans))

print('\n'.join(res))
    

        
