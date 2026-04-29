n, m = map(int, input().split())
def solve(n, m):
    if not (2 * m <= n <= (m * (m + 1) // 2 + 1)):
        return [-1]
    ans=[]
    for i in range(1,m+1):
        ans.append([i,i+1])
    n-=(m+1)
    nxt=m+2
    m-=1
    while n>0 and m>0:
        #贪心选择,最多可以用几个，就用几个，首先，深度是不能超过原来的m
        #然后还要剩下m-1个节点去挂载,
        cur=min(m,n-m+1)   
        ans.append([m-cur+1,nxt])
        nxt+=1
        for i in range(cur-1):
            ans.append([nxt-1,nxt])
            nxt+=1
        n-=cur
        m-=1
    return ans

res = solve(n, m)
if res[0] == -1:
    print("NO")
else:
    print("YES")
    for i in res:
        print(' '.join(map(str, i)))

