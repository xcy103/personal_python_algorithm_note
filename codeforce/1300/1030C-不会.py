import sys

n = int(input())
s = list(map(int,input()))
if sum(s)==0:
    if n>1:
        print('YES')
        exit(0)
    else:
        print('NO')
        exit(0)
#连续的部分
pre = 0
for i in range(n-1):
    pre+=s[i]
    if pre>0 and sum(s)%pre!=0:
        continue

    total = 0
    seg = 0
    f = 1
    for d in s:
        total+=d
        if total==pre:
            seg+=1
            total = 0
        elif total>pre:
            f = 0
            break
    if f and seg>1 and total==0:
        print('YES')
        exit(0)
print('NO')


import sys

n = int(input())
s = list(map(int, input().strip()))

total_sum = sum(s)

# 特判全为 0 的情况
if total_sum == 0:
    print("YES")
    exit(0)

# 第一段的长度可以从 1 到 n-1 
# 第一段的和 pre 分别可能为前缀和
current_pre = 0
for i in range(n - 1):
    current_pre += s[i]
    
    # 如果总和不能被当前前缀和整除，且总和不为0（已特判），那肯定分不均匀
    # 这一步可以剪枝，不加也能过
    if current_pre > 0 and total_sum % current_pre != 0:
        continue
        
    # 开始验证这个 pre 是否可行
    tmp_sum = 0
    segments = 0
    possible = True
    
    for digit in s:
        tmp_sum += digit
        if tmp_sum == current_pre:
            segments += 1
            tmp_sum = 0 # 满了一段，清空重来
        elif tmp_sum > current_pre:
            possible = False
            break
            
    # 如果顺利走完，且最后没有残留（tmp_sum == 0），并且分成了至少两段
    if possible and tmp_sum == 0 and segments >= 2:
        print("YES")
        exit(0)

print("NO")