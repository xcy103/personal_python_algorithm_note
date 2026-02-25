import sys
import heapq

# data = sys.stdin.read().split()
# n,m = int(data[0]), int(data[1])
# arr = []
# ptr = 2
# for i in range(m):
#     arr.append([int(data[ptr]), int(data[ptr+1])])
#     ptr+=2
n,m = map(int,sys.stdin.readline().split())
arr = []
for i in range(m):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort()
op = 0
s = 1
h = []
j = 0
while s <=n:
    while j < m and arr[j][0] <= s:
        heapq.heappush(h, -arr[j][1])
        j+=1
    
    if h:
        x = -heapq.heappop(h)

        if x >= s:
            op+=1
            s = x+1
            if s>=n+1:#这里我刚开始写了n，是不对的
                break
        elif x<s:
            op = -1
            break
    else:
        op = -1
        break
if s<=n:#这里刚开始少了判断，如果循环完了s没有超过n，说明没有完全覆盖
    op = -1
print(op)