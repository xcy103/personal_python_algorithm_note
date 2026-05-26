# import sys

# n,k,s = map(int,input().split())
# if s<k or (n-1)*k<s:
#     print('NO')
#     exit(0)

# avg = s//k
# left = s%k
# res = []
# for i in range(k):
#     if i%2==0:
#         res.append(avg+1)
#     else:
#         res.append(1)
# if k%2==0:
#     #最后一个是1
#     #需要之前的peak都是加2，然后最后一个1平掉多跳的
    
#     if left%2==0:
#         num2 = left//2
#         for i in range(0,k,2):
#             plus = min(num2,n-res[i])
#             res[i]+=plus
#             num2-=plus
#             if num2==0:
#                 break
#     else:
#         num2 = (left+1)//2
#         res[-1]+=1
#         for i in range(0,k,2):
#             plus = min(num2,n-res[i])
#             res[i]+=plus
#             num2-=plus
#             if num2==0:
#                 break
# else:
#     #最后一个数是peak
#     #先把前面凑齐再用最后一个平掉
#     if left%2==0:
#         num2 = left//2
#         for i in range(0,k-1,2):
#             plus = min(num2,n-res[i])
#             res[i]+=plus
#             num2-=plus
#             if num2==0:
#                 break
#     else:
#         num2 = (left+1)//2
#         res[-1]+=1
#         for i in range(0,k-1,2):
#             plus = min(num2,n-res[i])
#             res[i]+=plus
#             num2-=plus
#             if num2==0:
#                 break
# print('YES')
# print(*res)
#知道哪里错了，最后加1可能导致前两个一样了

import sys

n, k, s = map(int, input().split())
if s < k or (n - 1) * k < s:
    print('NO')
    exit(0)

avg = s // k
left = s % k

res = []
curr = 1 # 明确：从1开始跳

for i in range(k):
    # 这一步本来应该走 avg 距离
    step = avg
    
    # 前 left 步，每一步都要多走 1 距离
    if i < left:
        step += 1
        
    # 根据奇偶步决定跳跃方向
    if i % 2 == 0:
        # 偶数步（第1步、第3步...）：往右跳
        curr += step
    else:
        # 奇数步（第2步、第4步...）：往左跳
        curr -= step
        
    res.append(curr)

print('YES')
print(*res)


import sys

# 读取输入
n, k, s = map(int, sys.stdin.read().split())

# 基础排错：判断是否绝对不可能完成
if s < k or s > k * (n - 1):
    print('NO')
    exit(0)

print('YES')
curr = 1
res = []

for i in range(k):
    # 算一下走完这步之后，还剩几步
    rem_steps = k - 1 - i
    
    # 贪心取最大可能步长
    d = min(n - 1, s - rem_steps)
    
    # 能往右走就往右走，超出边界就往左走
    if curr + d <= n:
        curr += d
    else:
        curr -= d
        
    res.append(curr)
    s -= d  # 从总目标距离中扣除刚才走过的距离

print(*res)
