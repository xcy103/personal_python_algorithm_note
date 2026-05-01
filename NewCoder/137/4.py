for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    for i in range(1,n+1):
        s[i]=s[i-1]^a[i-1]
    dp=[0]+[1e18]*n
    for i in range(1,n+1):
        mn=1e18
        for j in range(i,0,-1):
            mn=min(mn,dp[j-1])
            dp[i]=min(dp[i],mn+(s[i]^s[j-1]))
    print(dp[n])