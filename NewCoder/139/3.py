import sys
from collections import deque
import queue
a,q = list(map(int,sys.stdin.readline().split()))
arr = list(map(int,sys.stdin.readline().split()))
que = []
for _ in range(q):
    que.append(list(map(int,sys.stdin.readline().split())))

#这里的arr是弹出的序列，
#感觉就是简单模拟就好
st = []
q = deque()
l = 0
f0 = 1
f1 = 1
for op in que:
    if len(op)==2:
        st.append(op[1])
        q.append(op[1])
    else:
        num1 = st.pop()
        num2 = q.popleft()
        if num1 != arr[l]:
            f0 = 0
        if num2 != arr[l]:
            f1 = 0
        if f0 or f1:
            l+=1
        else:
            print(-1)
            exit(0)
if f0 and f1:
    print('both')
    exit(0)
print('queue' if f1 else 'stack')