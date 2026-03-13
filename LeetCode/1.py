nums =[3,1,6,8,4]
target = 24
s = sum(nums)
if s!=2*target:
    print(False)

n = len(nums)
mask = 1<<n

for state in range(1,mask-1):
    tmp = 0
    for j in range(n):
        if state>>j&1:
            tmp+=nums[j]
    if tmp==target:
        print(True)
print(False)