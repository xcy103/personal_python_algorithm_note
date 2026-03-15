import sys
MOD = 10**9 + 7
k,q = map(int,sys.stdin.readline().split())
queries = list(map(int,sys.stdin.readline().split()))

nums = [1]*(10**6+1)

for i in range(k):
    nums[i] = 1
s = k
for i in range(k,10**6+1):
    nums[i] = s
    s = ((s-nums[i-k]+nums[i])%MOD+MOD)%MOD

res = []
for q in queries:
    res.append(nums[q-1])

print('\n'.join(map(str,res)))