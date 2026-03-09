#这道题就是字符串哈希+前缀和的经典运用，
#字符串哈希：如何快速得到字符串中任意子串的哈希值
# 1）选择一个质数做进制数，base
# 2）得到 base 的各个次方（在自然溢出下的结果），用 pow 数组记录
# 3）得到每个 i 位置的 hash[i]，
#   hash[i] = hash[i-1] * base + s[i] - 'a' + 1
# 4）子串 s[l…r] 的哈希值 =
#   hash[r] − hash[l−1] * base 的 (r−l+1) 次方，这道题用了左闭右开
from collections import defaultdict
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        base = 499
        n = len(s)
        word_len = len(words[0])
        word_cnt = len(words)
        total_len = word_len*word_cnt

        target = defaultdict(int)
        for w in words:
            target[self.hash_word(w,base)]+=1
        
        pow_base = [1]*(n+1)
        pre = [0]*n
        pre[0] = ord(s[0]) - ord('a') + 1
        for i in range(1,n):
            pre[i] = pre[i - 1] * base + ord(s[i]) - ord('a') + 1
        
        for i in range(1,n+1):
            pow_base[i] = pow_base[i - 1] * base

        def get_hash(l,r):
            res = pre[r-1]
            if l>0:
                res-=pre[l-1]*pow_base[r-l]
            return res
        
        ans = []
        # ------------------------------------------------
        # 按 word_len 进行分组滑动窗口
        # ------------------------------------------------
        for start in range(word_len):
            if start+total_len>n:
                break
            
            window = defaultdict(int)
            need = word_cnt
            left = start
            for _ in range(word_cnt):
                right = left+word_len
                h = get_hash(left,right)

                window[h]+=1
                if window[h]<=target[h]:
                    need-=1
                left = right
            if need == 0:
                ans.append(start)
            l1 = start
            r1 = l1 + word_len
            l2 = l1 + total_len
            r2 = l2 + word_len
            while r2<=n:
                out = get_hash(l1,r1)
                window[out]-=1
                if window[out]<target[out]:
                    need+=1
                
                enter = get_hash(l2,r2)
                window[enter]+=1
                if window[enter]<=target[enter]:
                    need-=1
                if need == 0:
                    ans.append(r1)
                l1+=word_len
                r1+=word_len
                l2+=word_len
                r2+=word_len
        return ans
    def hash_word(self,word,base):
        h = 0
        for ch in word:
            h = base*h + (ord(ch) - ord('a') + 1)
        return h

