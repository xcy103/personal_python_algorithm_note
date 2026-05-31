import sys

n,k = map(int,input().split())
s = input()

# 计算最长 prefix == suffix
lps = [0]*n
j = 0
for i in range(1,n):
    while j>0 and s[i]!=s[j]:
        j = lps[j-1]
    if s[i]==s[j]:
        j+=1
    lps[i]=j

overlap = lps[-1]

# 构造答案
res = s
add = s[overlap:]
for _ in range(k-1):
    res += add

print(res)