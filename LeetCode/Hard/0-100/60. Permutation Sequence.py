class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        nums = list(range(1, n+1))
        k -= 1  # 转成 0-index
        
        res = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i-1)
            idx = k // fact
            k %= fact
            
            res.append(str(nums[idx]))
            nums.pop(idx)
        
        return ''.join(res)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        # 树状数组
        tree = [0] * (n + 1)
        
        def add(i, v):
            while i <= n:
                tree[i] += v
                i += i & -i
        
        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s
        
        # 找第k小
        def find_kth(k):
            pos = 0
            bit = 1 << (n.bit_length())  # 最大2^x
            
            while bit:
                nxt = pos + bit
                if nxt <= n and tree[nxt] < k:
                    k -= tree[nxt]
                    pos = nxt
                bit >>= 1
            
            return pos + 1
        
        # 初始化
        for i in range(1, n + 1):
            add(i, 1)
        
        k -= 1
        res = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            idx = k // fact + 1  # 第 idx 小（注意+1）
            k %= fact
            
            num = find_kth(idx)
            res.append(str(num))
            
            add(num, -1)  # 删除
        
        return ''.join(res)