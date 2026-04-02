# v2.1的模板不一定对
import heapq
import math
from collections import defaultdict,deque
from itertools import groupby
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res = []
        l = list(map(int,str(low)))
        h = list(map(int,str(high)))
        n = len(h)
        diff = n-len(l)
        path = []
     
        def f(i,limit_low,limit_high,pre):
            nonlocal path,res
            if i==n:
                if pre!=10:
                    num = 0
                    for x in path:
                        num = 10*num+x
                    res.append(num)
                return
            
            lo = l[i-diff] if limit_low and i>=diff else 0
            hi = h[i] if limit_high else 9

            # 👉 跳过前导位（你原逻辑保留）
            if limit_low and i<diff:
                f(i+1,True,False,pre)

            for d in range(lo,hi+1):

                # 🚫 防止 leading zero
                if pre==10 and d==0:
                    continue

                if pre==10:
                    path.append(d)
                    f(
                        i+1,
                        limit_low and i>=diff and d==lo,
                        limit_high and d==hi,
                        d
                    )
                    path.pop()
                else:
                    if abs(d-pre)==1:
                        path.append(d)
                        f(
                            i+1,
                            limit_low and i>=diff and d==lo,
                            limit_high and d==hi,
                            d
                        )
                        path.pop()
            return 

        f(0,True,True,10)
        if low==0:
            res.append(0)
        res.sort()
        return res