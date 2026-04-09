def uniquePaths(g) -> int:
    MOD = 10**9+7
    m,n = len(g),len(g[0])
    #1向下，2向右
    
    #@cache
    def f(i,j,d):
        if i<0 or j<0 or i>=m or j>=n:
            return 0
        if i==m-1 and j==n-1:
            return 1
        ans = 0
        if d==0 or g[i][j]==0:
            ans = (f(i+1,j,1)+f(i,j+1,0))%MOD
        elif d==1:
            ans+=f(i+1,j,2)
        elif d==2:
            ans+=f(i,j+1,1)
        return ans%MOD
    ans = f(0,0,0)
    #f.cache_clear()
    return ans%MOD
uniquePaths([[0,1,1],[1,1,0]])