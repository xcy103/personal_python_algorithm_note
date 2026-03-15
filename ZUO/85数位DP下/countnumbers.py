#不要被模板局限思路，其实就是从低到高讨论

class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        
        def count(num,d):
            if num<=0:
                return 0
            ans = 0
            right = 1
            tmp = num
            while tmp:
                left = tmp//10
                cur = tmp%10
                if d==0:
                    left-=1
                ans += left*right
                if cur>d:
                    ans+=right
                elif cur==d:
                    ans+=num%right+1
                right*=10
                tmp//=10
            return ans
        return count(high,d) - count(low-1,d)