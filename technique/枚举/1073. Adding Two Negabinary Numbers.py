from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry:
            a = arr1[i] if i >= 0 else 0
            b = arr2[j] if j >= 0 else 0
            
            s = a + b + carry
            
            res.append(s & 1)          # 当前位
            carry = -(s >> 1)          # 关键
            
            i -= 1
            j -= 1
        
        # 去掉前导0
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return res[::-1]