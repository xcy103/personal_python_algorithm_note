import sys

n = int(input())
s = list(input().split()[0])

#就是统计mod 3 的颜色数量
c0 = [0]*3
c1 = [0]*3
c2 = [0]*3
for i in range(0,n,3):
    if s[i]=='R':
        c0[0]+=1
    elif s[i]=='G':
        c0[1]+=1
    elif s[i]=='B':
        c0[2]+=1

for i in range(1,n,3):
    if s[i]=='R':
        c1[0]+=1
    elif s[i]=='G':
        c1[1]+=1
    elif s[i]=='B':
        c1[2]+=1
for i in range(2,n,3):
    if s[i]=='R':
        c2[0]+=1
    elif s[i]=='G':
        c2[1]+=1
    elif s[i]=='B':
        c2[2]+=1
#还需要颜色不一样，三个下标需要颜色不一样
#直接暴力
ans = ""
nums = 10**18
mp = ['R','G','B']
tmp = sum(c0)+sum(c1)+sum(c2)
for i in range(3):
    for j in range(3):
        if i==j:continue
        for k in range(3):
            if i==k or k==j:continue
            if tmp-c0[i]-c1[j]-c2[k]<nums:
                nums = tmp-c0[i]-c1[j]-c2[k]
                res = [0]*n
                for p in range(0,n,3):
                    res[p] = mp[i]
                for p in range(1,n,3):
                    res[p] = mp[j]
                for p in range(2,n,3):
                    res[p] = mp[k]
                ans = ''.join(res)
print(nums)
print(ans)
