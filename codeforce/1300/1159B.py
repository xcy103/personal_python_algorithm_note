import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

nums = []
for i,x in enumerate(arr):
    nums.append((x,i))

nums.sort()

mx = [0]*n
mn = [0]*n

mn[-1] = nums[-1][1]
mx[-1] = nums[-1][1]

for i in range(n-2,-1,-1):
    mx[i] = max(mx[i+1], nums[i][1])
    mn[i] = min(mn[i+1], nums[i][1])

ans = 10**18

for i in range(n-1):
    val, idx = nums[i]
    d = max(abs(idx - mn[i+1]), abs(idx - mx[i+1]))
    if d == 0:
        continue
    ans = min(ans, val // d)

print(ans)