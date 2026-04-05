from itertools import accumulate
def maxValue(nums):
    n = len(nums)
    res = [0]*n
    mx = [0]*n
    mx[0] = nums[0]
    for i in range(1,n):
        mx[i] = max(mx[i-1],nums[i])
    res[0] = mx[0]
    for i in range(1,n):
        res[i] = max(mx[i-1],nums[i])
    #树状数组查询比自己小的，跳到的最大值
    s = sorted(set(nums))
    rank = {v:i+1 for i,v in enumerate(s)}
    arr = []
    for i in range(n):
        arr.append((rank[nums[i]],res[i]))
    tree = [0]*(n+1)
    def update(i,v):
        while i<=n:
            tree[i] = max(tree[i],v)
            i+=i&-i
    def query(i):
        ans = 0
        while i>0:
            ans = max(tree[i],ans)
            i&=i-1
        return ans
    #这里x=res[idx]
    for idx in range(n-1,-1,-1):
        i = arr[idx][0]
        res[idx] = max(res[idx],query(i-1))
        update(i,res[idx])
    return res
    
maxValue([30,21,5,35,24])