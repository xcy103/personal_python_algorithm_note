import sys

class SegmentTree:

    def __init__(self):
        self.MAXN = 100005
        self.arr = [0]*self.MAXN
        self.sum_arr = [0]*(self.MAXN<<2)
        self.add_arr = [0]*(self.MAXN<<2)
    
    def up(self,i):
        self.sum_arr[i] = self.sum_arr[i<<1] + self.sum_arr[i<<1 | 1]
    
    def lazy(self,i,v,n):
        self.sum_arr[i] += v*n
        self.add_arr[i] += v
    
    def down(self,i,ln,rn):
        if self.add_arr[i]:
            self.lazy(i<<1,self.add[i],ln)
            self.lazy(i<<1|1,self.add_arr[i],rn)
            self.add_arr[i] = 0
    
    def build(self,l,r,i):
        if l==r:
            self.sum_arr[i] = self.arr[l]
        else:
            mid = (l+r)>>1
            self.build(l,mid,i<<1)
            self.build(mid+1,r,1<<i|1)
            self.up(i)
        self.add_arr[i] = 0
    
    def update(self,jobl,jobr,jobv,l,r,i):
        if jobl<=l and r<=jobr:
            self.lazy(i,jobv,r-l+1)
        else:
            mid = (l+r)>>1
            self.down(i,mid - l + 1,r - mid)
            if jobl<=mid:
                self.update(jobl,jobr,jobv,l,mid,i<<1)
            if jobr>mid:
                self.update(jobl,jobr,jobv,mid+1,r,i<<1|1)
            self.up(i)
    
    def query(self,jobl,jobr,l,r,i):
        if jobl<=l and r<=jobr:
            return self.sum_arr[i]
        mid = (l+r)>>1
        self.down(i,mid - l + 1,r - mid)
        ans = 0
        if jobl<=mid:
            ans+=self.query(jobl,jobr,l,mid,i<<1)
        if jobr>mid:
            ans+=self.query(jobl,jobr,mid+1,r,i<<1|1)
        return ans