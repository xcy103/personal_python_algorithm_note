class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        c0 = 0
        c1 = 0
        for i in range(n):
            if nums[i]%2:
                c1+=1
                nums[i] = 1
            else:
                c0+=1
                nums[i] = 0

        if not (c0==c1 or abs(c0-c1)==1):
            return -1
        idx = [i for i,x in enumerate(nums) if x==1]

        def f(start):
            if (n-start+1)//2!=len(idx):
                return inf
            return sum(abs(i-j) for i,j in zip(range(start,n,2),idx))
        
        return min(f(0),f(1))

        


                 
        