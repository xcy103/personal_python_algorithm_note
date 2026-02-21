import sys
import heapq

n = int(sys.stdin.readline().strip())
ans = []
for _ in range(n):
    t,d = map(int, sys.stdin.readline().split())
    buy = list(map(int, sys.stdin.readline().split()))
    use = list(map(int, sys.stdin.readline().split()))
    h = []
    for i in range(t):
        heapq.heappush(h,(i,buy[i]))
        s = use[i]
        while h and s>=h[0][1]:
            s -= h[0][1]
            heapq.heappop(h)
        if h and s<=h[0][1]:
            day,left = heapq.heappop(h)
            left-=s
            heapq.heappush(h,(day,left))
        
        while h and i - h[0][0]>=d:
            heapq.heappop(h)
    s = 0
    while h:
        s+=h[0][1]
        heapq.heappop(h)
    ans.append(s)

print(*ans)