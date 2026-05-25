class Solution:
    def powerUpdate(self, nums: list[int], p: int, queries: list[list[int]]) -> list[int]:
        mod = 10**9+7

        vals = nums[:]
        for v,_ in queries:
            vals.append(v)
        vals = sorted(set(vals))
        mp = {v:i+1 for i,v in enumerate(vals)}

        n = len(vals)
        t_mask = 1<<(n.bit_length())
        tree = [0]*(n+1)

        def add(i,v):
            while i<=n:
                tree[i]+=v
                i+=i&-i
        
        def kth(k):
            #找第k小
            pos = 0
            mask = t_mask
            while mask:
                nxt = pos + mask
                if nxt<=n and tree[nxt]<k:
                    k-=tree[nxt]
                    pos = nxt
                mask>>=1
            return pos+1
        cnt = 0
        for x in nums:
            add(mp[x],1)
            cnt+=1
        res = []
        for v,k in queries:
            add(mp[v],1)
            cnt+=1
            idx = kth(cnt-k+1)
            x = vals[idx-1]
            p = pow(p,x,mod)
            res.append(p)
        return res