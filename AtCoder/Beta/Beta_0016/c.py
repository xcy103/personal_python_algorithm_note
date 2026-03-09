import sys
n,l,r,t = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    p,s = map(int,sys.stdin.readline().split())
    arr.append([p,s])
nums = []
for i,[p,s] in enumerate(arr):
    if l<=p<=r and s>=t:
        nums.append([p,s,i])

nums.sort(key = lambda x:(x[0],-x[1],x[2]))
if len(nums)==0:
    print(-1)
else:
    print(nums[0][2] + 1)