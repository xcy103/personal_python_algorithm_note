import sys
input = sys.stdin.readline
#感觉这道题纯属我想多了
mod = 998244353

n = int(input())
s = input().strip()

# 统计前缀连续相同
l = 0
while l < n and s[l] == s[0]:
    l += 1

# 统计后缀连续相同
r = n - 1
while r >= 0 and s[r] == s[-1]:
    r -= 1

r = n - 1 - r  # 后缀长度

# 情况1：首尾相同
if s[0] == s[-1]:
    # (l+1)*(r+1)
    print((l + 1) * (r + 1) % mod)
else:
    # l + r + 1
    print((l + r + 1) % mod)