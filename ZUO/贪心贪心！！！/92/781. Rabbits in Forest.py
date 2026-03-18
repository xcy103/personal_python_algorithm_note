#这道题就是观察规律，先统计频次，假如有4个三，我么可以补充一只兔子
#相当于这次个兔子互相说颜色相同，如果有5个三，那就是4个4个为一组，再补充三个兔子
#
from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        c = Counter(answers)
        op = 0
        for k,v in c.items():
            op+=(v+k)//(k+1) * (k+1)
        return op