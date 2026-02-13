import sys

class SegmentTreeUpdateAddQueryMax:

    def __init__(self):
        self.MAXN = 100005
        self.arr = [0]*(self.MAXN)
        self.add_arr = [0]*(self.MAXN<<2)
        self.max_val = [0]*(self.MAXN<<2)
        self.change_arr = [0]*(self.MAXN<<2)
        self.update_flag = [0]*(self.MAXN<<2)

    def up(self,i):
        self.max_val[i] = max(self.max_val[i << 1], self.max_val[i << 1 | 1])    
    def down(self,i):
        if self.update_flag[i]:
            self.lazy_update(i<<1,self.change_arr[i])
            self.lazy_update(i<<1|1,self.change_arr[i])
            self.update_flag[i] = False
        
        if self.add_arr[i]:
            self.lazy_add(i << 1, self.add_arr[i])
            self.lazy_add(i << 1 | 1, self.add_arr[i])
            self.add_arr[i] = 0
    
    def lazy_update(self,i,v):
        self.max_val[i] = v
        self.add_arr[i] = 0
        self.change_arr[i]  =v
        self.update_flag[i] = True
    
    def lazy_add(self,i,v):
        self.max_val[i] += v
        self.add_arr[i] += v
    
    def build(self,l,r,i):
        if l==r:
            self.max_val[i] = self.arr[i]
        else:
            mid = (l+r)>>1
            self.build(l,mid,i<<1)
            self.build(mid+1,r,i<<1|1)
            self.up(i)
        self.add_arr[i] = 0
        self.change_arr[i] = 0
        self.update_flag[i] = False
    
    def update_range(self,jobl,jobr,jobv,l,r,i):
        if jobl<=l and r<=jobr:
            self.lazy_update(i,jobv)
        else:
            mid = (l+r)>>1
            self.down(i)
            if jobl<=mid:
                self.update_range(jobl,jobr,jobv,l,mid,i<<1)
            if jobr>mid:
                self.update_range(jobl,jobr,jobv,mid+1,r,i<<1|1)
            self.up(i)
    
    def add_range(self,jobl,jobr,jobv,l,r,i):
        if jobl<=l and r<=jobr:
            self.lazy_add(i,jobv)
        else:
            mid = (l+r)>>1
            self.down(i)
            if jobl<=mid:
                self.add_range(jobl,jobr,jobv,l,mid,i<<1)
            if jobr>mid:
                self.add_range(jobl,jobr,jobv,mid+1,r,i<<1|1)
            self.up(i)
    def query(self,jobl,jobr,l,r,i):
        if jobl<=l and r<=jobr:
            return self.max_val[i]
        else:
            mid = (l+r)>>1
            self.down(i)
            ans = float('-inf')
            if jobl<=mid:
                ans = max(ans,self.query(jobl,jobr,l,mid,i<<1))
            if jobr>mid:
                ans = max(ans,self.query(jobl,jobr,mid+1,r,i<<1|1))
            return ans


