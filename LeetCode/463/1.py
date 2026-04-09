from itertools import accumulate
def maxProfit(p, s, k):
 
    n = len(p)
    pre = [0]*(n+1)
    for i in range(n):
        pre[i+1] = pre[i]+p[i]*s[i]
    ppre = [0]+list(accumulate(p))
    num = pre[-1]
    ans = ppre[-1]
    for i in range(n-k+1):
        l = i
        mid = i+k//2
        r = i+k-1
        ans = max(ans,num - (pre[r+1]-pre[l])+ppre[r+1]-ppre[mid])
    return ans

maxProfit([5,4,3],[1,1,0],2)