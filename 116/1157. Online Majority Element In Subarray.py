from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List
# 先用线段树维护水王信息，然后选出候选人，再用二分判断是否符合标准

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.pos = defaultdict(list)
        for idx,val in enumerate(arr):
            self.pos[val].append(idx)
        
        self.cand_tree = [0]*(self.n<<2)
        self.hp_tree = [0]*(self.n<<2)
        self.build(arr,1,0,self.n-1)
    
    def up(self,i):
        l,r = i<<1,i<<1|1
        cand,hp = self.cand_tree,self.hp_tree
        lc,lh = cand[l],hp[l]
        rc,rh = cand[r],hp[r]
        if lc==rc:
            cand[i] = lc
            hp[i] = rh+lh
        elif lh>=rh:
            cand[i] = lc
            hp[i] = lh-rh
        else:
            cand[i] = rc
            hp[i] = rh-lh
    
    def build(self,arr,i,l,r):
        cand,hp = self.cand_tree,self.hp_tree
        if l==r:
            cand[i] = arr[l]
            hp[i] = 1
            return
        
        mid = (l+r)>>1
        self.build(arr,i<<1,l,mid)
        self.build(arr,i<<1|1,mid+1,r)
        self.up(i)
            
    def query_tree(self,jobl,jobr,l,r,i):
        cand,hp = self.cand_tree,self.hp_tree
        if jobl<=l and jobr>=r:
            return cand[i],hp[i]
        mid = (l+r)>>1
        if jobr<=mid:
            return self.query_tree(jobl,jobr,l,mid,i<<1)
        if jobl>mid:
            return self.query_tree(jobl,jobr,mid+1,r,i<<1|1)
        lc,lh = self.query_tree(jobl,jobr,l,mid,i<<1)
        rc,rh = self.query_tree(jobl,jobr,mid+1,r,i<<1|1)
        if lc==rc:
            return lc,lh+rh
        elif lh >= rh:
            return lc, lh - rh
        else:
            return rc, rh - lh
        
    def query(self, left: int, right: int, threshold: int) -> int:
        cand,_ = self.query_tree(left,right,0,self.n-1,1)
        idx_list = self.pos[cand]
        # 找到第一个 >= left 的位置
        l= bisect_left(idx_list, left)
        # 找到第一个 > right 的位置
        r = bisect_right(idx_list, right)

        return cand if r-l >= threshold else -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)