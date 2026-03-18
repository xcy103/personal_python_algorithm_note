#关注最大词频
#根据最大词频分配，因为你思考一下，我们肯定是要分配最大词频个数组
from collections import Counter
from typing import List
class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        c = Counter(nums)
        return n//max(c.values())>=k