from bisect import bisect_right
from itertools import accumulate
def kthRemainingInteger(nums: list[int], queries: list[list[int]]) -> list[int]:
    n = len(nums)
    #其实就是查询区间l,r对应在nums里面，
    #有多少个小于等于2*k的偶数
    arr = []
    for x in nums:
        arr.append(1 if x%2==0 else 0)

    pre = [0] + list(accumulate(arr))
    
    def f(mid,l,r):
        idx = bisect_right(arr,2*(k+mid),l,r)
        return pre[idx]-pre[l]>=mid
        
    res = [0]*len(queries)
    for i,[l,r,k] in enumerate(queries):
        tl = -1
        tr = n
        while tl+1<tr:
            mid = (tl+tr)//2
            if f(mid,l,r+1): tr = mid
            else: tl = mid
        res[i] = 2*(k+tr)
    return res
kthRemainingInteger([4,6,22,24],[[0,2,10],[0,3,13]])