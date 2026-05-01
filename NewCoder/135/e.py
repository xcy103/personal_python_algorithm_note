#思路就是，最多操作两次，就可以使得相邻不同

import sys

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    if n==1:
        res.append('0')
        continue
    dp = [[10**18]*5 for _ in range(n)]
    if a[0]-2>=1:
        dp[0][0]=c[0]<<1
    if a[0]-1>=1:
        dp[0][1]=c[0]
    dp[0][2]=0
    dp[0][3]=b[0]
    dp[0][4]=b[0]<<1

    for i in range(1,n):
        for k1 in range(-2,3):
            for k2 in range(-2,3):
                if a[i]+k1==a[i-1]+k2 or a[i]+k1<1:continue
                 
                if k1<0:
                    dp[i][k1+2]=min(dp[i][k1+2],dp[i-1][k2+2]+abs(k1)*c[i])
                else:
                    dp[i][k1+2]=min(dp[i][k1+2],dp[i-1][k2+2]+k1*b[i])
    res.append(str(min(dp[-1])))

print('\n'.join(res))

