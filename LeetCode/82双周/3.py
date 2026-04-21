from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        """
        题目意思：
        给你两个数组 nums1 和 nums2
        
        定义：
        👉 差值平方和 = Σ (nums1[i] - nums2[i])^2
        
        操作：
        - 你可以对 nums1 中任意元素 +1 或 -1，最多 k1 次
        - 你可以对 nums2 中任意元素 +1 或 -1，最多 k2 次
        👉 总操作次数最多 k = k1 + k2
        
        目标：
        👉 让最终的“差值平方和”最小
        
        
        等价转化：
        - 只关心 diff[i] = |nums1[i] - nums2[i]|
        - 每次操作本质是：让某个 diff -= 1
        - 总共最多做 k 次
        
        
        数据范围：
        - 1 <= n <= 1e5
        - 0 <= nums[i] <= 1e5
        - 0 <= k1, k2 <= 1e9
        
        
        核心流程（简述）：
        - 计算所有 diff
        - 用 Counter 统计每个差值的频率
        - 从大到小排序（优先减大的）
        - 按“层”往下降：
            - 如果 k 足够 → 整层下降
            - 不够 → 均匀分配（关键）
        - 最后计算平方和
        
        
        关键点：
        - 桶/频率压缩（避免 O(n log n * k)）
        - 批量处理（按层削）
        """

        k = k1 + k2
        
        # 计算差值
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # 统计频率
        cnt = Counter(diff)
        
        # 按差值从大到小排序
        arr = sorted(cnt.items(), reverse=True)
        
        # 哨兵（方便处理最后一层）
        arr.append((0, 0))
        
        for i in range(len(arr) - 1):
            v, c = arr[i]
            v2, _ = arr[i + 1]
            
            # 把当前层降到下一层需要的操作数
            need = (v - v2) * c
            
            if k >= need:
                # 可以全部降到下一层
                k -= need
                arr[i + 1] = (v2, arr[i + 1][1] + c)
            else:
                # 不够 → 均匀分配（关键）
                d = k // c
                r = k % c
                
                res = 0
                
                # (c - r) 个降到 v - d
                res += (c - r) * (v - d) ** 2
                
                # r 个降到 v - d - 1
                res += r * (v - d - 1) ** 2
                
                # 后面的直接累加
                for j in range(i + 1, len(arr)):
                    val, cntt = arr[j]
                    res += cntt * val * val
                
                return res
        
        # 如果全部削到 0
        return 0