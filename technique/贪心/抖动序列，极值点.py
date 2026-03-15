# 【笔记】最长抖动子序列 / 
# 乱翘数组1. 核心思路这题就是找“折线图”里的所有拐点（波峰和波谷）。
# 因为要删掉最少的数，所以我们要留住尽可能多的“尖尖”。
# 2. 解题步骤第一步：去重。连续相同的数（如 2, 2, 2）只保留一个，变成 [2]。
# 第二步：找尖尖。看中间的数 $a[i]$ 是不是比左右两边都大，或者比左右两边都小。
# 第三步：算个数。保留的长度 = 所有的“尖尖” + 开头 1 个 + 末尾 1 个。
# 第四步：算答案。删除个数 = 原数组总长 - 保留的长度。
# 3. 判定公式（逻辑核心）如果去重后的数组里：
# (a[i] > a[i-1] && a[i] > a[i+1])  -> 这是波峰，留着。
# (a[i] < a[i-1] && a[i] < a[i+1])  -> 这是波谷，留着。
# 4. 复杂度时间：$O(N)$，扫一遍就出结果。
# 空间：$O(N)$，存一下去重后的数组（或者直接在原数组上双指针操作降到 $O(1)$）。
#找了一道leetcode类似题目https://leetcode.com/problems/wiggle-subsequence/
from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        arr = []
        arr.append(nums[0])
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                arr.append(nums[i])
        p1 = n - len(arr)
        c = 1
        pre = 0
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if (diff>0 and pre<=0) or ( diff<0 and pre>=0):
                c+=1
                pre = diff
        return c
