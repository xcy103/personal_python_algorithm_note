from typing import List
MOD = 10**9+7
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        fact = [1]*(n+1)
        inv = [1]*(n+1)
        for i in range(2,n+1):
            fact[i] = fact[i-1]*i%MOD
        inv[n] = pow(fact[n],MOD-2,MOD)
        for i in range(n-1,0,-1):
            inv[i] = (i+1)*inv[i+1]%MOD
        res = 0
        for i in range(n):
            l = n-i
            for j in range(0,min(k,l)):
                res = (res+fact[l-1]*inv[j]*inv[l-1-j]*nums[i])%MOD
        nums.reverse()
        for i in range(n):
            l = n-i
            for j in range(0,min(k,l)):
                res = (res+fact[l-1]*inv[j]*inv[l-1-j]*nums[i])%MOD
        return res
        