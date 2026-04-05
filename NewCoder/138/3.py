import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    _ = int(sys.stdin.readline().strip())
    arr.append(list(map(int, sys.stdin.readline().split())))

def f(x,y):
    s = list(str(x))
    ans = 0
    while int(''.join(s))>y:
        ans+=1
        s = list(str(sum(list(map(int,s)))))
        if len(s)==1 and int(s[0])>y:
            return -1,-1
    return ans,int(''.join(s))
res = []
for nums in arr:
    l = len(nums)
    op = 0
    tag = 1
    for i in range(l-2,-1,-1):
        if nums[i]>nums[i+1]:
            ans,num = f(nums[i],nums[i+1])
            if ans == -1:
                res.append(str(-1))
                tag = 0
                break
            op+=ans
            nums[i] = num
    if tag:
        res.append(str(op))
print('\n'.join(res))
