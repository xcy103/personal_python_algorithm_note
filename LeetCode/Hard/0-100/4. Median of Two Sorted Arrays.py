class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)

        def bf(A,B,k):
            if len(A)>len(B):
                return bf(B,A,k)
            
            if not A:
                return B[k-1]
            
            if k==1:
                return min(A[0],B[0])
            
            i = min(len(A),k//2)
            j = k-i
            if A[i-1]<B[j-1]:
                return bf(A[i:],B,k-i)
            else:
                return bf(A,B[j:],k-j)
        
        if l%2==1:
            return bf(nums1,nums2,(l+1)//2)
        else:
            fir = bf(nums1,nums2,l//2)
            sec = bf(nums1,nums2,l//2+1)
            return (fir+sec)/2.0
        

# 
# # Median of Two Sorted Arrays（极简版）

# ## 思路
# 👉 转化为：找第 k 小元素

# - 奇数：第 (l+1)//2 小
# - 偶数：平均第 l//2 和 l//2+1 小

# ---

# ## 核心（bf）

# ```

# bf(A, B, k):
# 保证 A 短

# ```
# 若 A 为空 → 返回 B[k-1]
# 若 k == 1 → 返回 min(A[0], B[0])

# i = min(len(A), k//2)
# j = min(len(B), k//2)

# 若 A[i-1] < B[j-1]:
#     丢 A 前 i 个 → bf(A[i:], B, k-i)
# 否则：
#     丢 B 前 j 个 → bf(A, B[j:], k-j)
# ```

# ```

# ---

# ## 一句话
# 👉 每次比较第 k/2 个，小的那边直接丢一半
# ```
