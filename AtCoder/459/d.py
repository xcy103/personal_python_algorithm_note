# import sys
# from collections import Counter
# from heapq import heappop,heappush
# t = int(input())


# ans = []
# for _ in range(t):
#     s = list(input().strip())
#     #开始判断时候可以交替排列
#     c = Counter(s)
#     n = len(s)
#     k = max(c.values())
#     if k>n-k+1:
#         ans.append(['No'])
#         continue
#     #怎么排列呢
#     h = []
#     for key,val in c.items():
#         heappush(h,(-val,key))
#     res = []
#     while h:
#         v1,c1 = heappop(h)
#         if not h:
#             res.append(c1)
#             break
#         v2,c2 = heappop(h)
#         res.append(c1)
#         res.append(c2)
#         if v1+1<0:
#             heappush(h,(v1+1,c1))
#         if v2+1<0:
#             heappush(h,(v2+1,c2))
#     ans.append(['Yes',''.join(res)])
# for nums in ans:
#     if len(nums)==1:
#         print('No')
#     else:
#         print('Yes')
#         print(nums[1])


#=============================
import sys
from collections import Counter

t = int(input())

ans = []
for _ in range(t):
    s = list(input().strip())
    c = Counter(s)
    n = len(s)
    k = max(c.values())
    
    # 保持你原有的合法性判定
    if k > n - k + 1:
        ans.append(['No'])
        continue
    
    # === 优化部分：替代原有的 Heap 逻辑 ===
    # 1. 按照频次从大到小对字符进行排序
    sorted_chars_with_freq = c.most_common()
    
    # 2. 将其展开为完整的字符列表，例如 [('a', 3), ('b', 1)] -> ['a', 'a', 'a', 'b']
    sorted_chars = []
    for char, freq in sorted_chars_with_freq:
        sorted_chars.extend([char] * freq)
    
    # 3. 创建结果数组，利用双指针或步长隔位填充
    res = [None] * n
    
    # 优先填偶数位 0, 2, 4 ...
    p = 0
    for i in range(0, n, 2):
        res[i] = sorted_chars[p]
        p += 1
    # 再填奇数位 1, 3, 5 ...
    for i in range(1, n, 2):
        res[i] = sorted_chars[p]
        p += 1
    # ===================================
        
    ans.append(['Yes', ''.join(res)])

# 保持你原有的输出逻辑不变
for nums in ans:
    if len(nums) == 1:
        print('No')
    else:
        print('Yes')
        print(nums[1])