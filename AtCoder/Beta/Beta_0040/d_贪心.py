import sys
from heapq import heappop,heappush
n,g,f = list(map(int,sys.stdin.readline().split()))
pos = []
for _ in range(n):
    pos.append(list(map(int,sys.stdin.readline().split())))
pos.sort()

l = 0
cur = f
h = []
op = 0
# while l<n and cur<g:
#     while l<n and pos[l][0]<=cur:
#         heappush(h,-pos[l][1])
#         l+=1
#     #如果能进入循环，就代表cur<g
#     #加入堆之后，如果没有能够加油的地方，就代表无法到达
#     if not h:
#         break
#     if h and cur<g:
#         cur+=-heappop(h)
#         op+=1
#     # if not h and ((l==n and cur<g) or (l<n and cur<pos[l][0])):
#     #     break
#     #我之前是这么写的，但是对，我也不知道哪里不对，反正就是复杂了
# print(op if cur>=g else -1)
# 只需要判断是否还没有到达终点
#错了错了，如果堆里还有加油站，就还需要
while cur < g:
    # 把当前油量能到达的所有加油站都放进堆里
    while l < n and pos[l][0] <= cur:
        heappush(h, -pos[l][1])
        l += 1
        
    # 如果堆是空的，说明能到达的加油站都加过了，还是到不了下一步，直接退出
    if not h:
        break
        
    # 从堆里拿出能加的最多油量加上
    cur += -heappop(h)
    op += 1
    
print(op if cur >= g else -1)