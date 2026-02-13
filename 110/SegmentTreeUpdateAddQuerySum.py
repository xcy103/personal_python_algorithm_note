import sys

class SegmentTreeUpdateAddQuerySum:
    def __init__(self):
        self.MAXN = 100005
        self.arr = [0]*self.MAXN
        self.sum_arr = [0]*(self.MAXN<<2)
        self.add_arr = [0]*(self.MAXN<<2)
        self.change_arr = [0]*(self.MAXN<<2)
        self.update_flag = [False]*(self.MAXN<<2)
    
    def up(self,i):
        self.sum_arr[i] = self.sum_arr[i<<1]+self.sum_arr[i<<1|1]

    def down(self,i,ln,rn):
        if self.update_flag[i]:
            self.lazy_update(i<<1,self.change[i],ln)
            self.lazy_update(i<<1|1,self.change[i],rn)
            self.update_flag[i] = False
        
        if self.add_arr[i]:
            self.lazy_add(i<<1,self,self.add_arr[i],ln)
            self.lazy_add(i<<1|1,self,self.add_arr[i],rn)
            self.add_arr[i] = 0
    
    def lazy_update(self,i,v,n):
        self.sum_arr[i] = v*n
        self.change_arr[i] = v
        self.update_flag[i] = True
        self.add[i] = 0
    
    def lazy_add(self,i,v,n):
        self.sum_arr[i] += v*n
        self.add_arr[i] += v
    
    def build(self,l,r,i):
        if l==r:
            self.sum_arr[i] = self.arr[l]
        else:
            mid = (l+1)>>1
            self.build(l,mid,i<<1)
            self.build(mid+1,r,i<<1|1)
            self.up(i)
        self.add_arr[i] = 0
        self.change_arr[i] = 0
        self.update_flag[i] = False
    
    def update_range(self,jobl,jobr,jobv,l,r,i):
        if jobl<=l and r<=jobr:
            self.lazy_update(i,jobv,r-l+1)
        else:
            mid = (l+r)>>1
            self.down(i,mid - l + 1,r - mid)
            if jobl<=mid:
                self.update_range(jobl,jobr,jobv,l,mid,i<<1)
            if jobv>mid:
                self.update_range(jobl,jobr,jobv,mid+1,r,i<<1|1)
            self.up(i)
    
    def add_range(self,jobl,jobr,jobv,l,r,i):
        if jobl<=l and r<=jobr:
            self.add_update(i,jobv,r-l+1)
        else:
            mid = (l+r)>>1
            self.down(i,mid - l + 1,r - mid)
            if jobl<=mid:
                self.add_range(jobl,jobr,jobv,l,mid,i<<1)
            if jobv>mid:
                self.add_range(jobl,jobr,jobv,mid+1,r,i<<1|1)
            self.up(i)
    
    def query(self,jobl,jobr,jobv,l,r,i):
        if jobl <= l and r <= jobr:
            return self.sum_arr[i]
        else:
            mid = (l+r)>>1
            self.down(i,mid-l+1,r-mid)
            ans = 0
            if jobl <= mid:
                ans += self.query(jobl, jobr, l, mid, i << 1)
            if jobr > mid:
                ans += self.query(jobl, jobr, mid + 1, r, i << 1 | 1)
            return ans