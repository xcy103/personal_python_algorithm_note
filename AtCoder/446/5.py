import sys

M,A,B = map(int,sys.stdin.readline().split())


# x = 0
# y = 3
# for i in range(10):
#     x,y = y,A*y+B*x
#     print(y,y%M)

op = 0
for x in range(M):
    for y in range(M):
        if x==0 or y==0:
            continue
        # ans = []
        # for i in range(2):
        #     x,y = y,A*y+B*x
        #     ans.append(y)
        t = A*y+B*x
        if (t)%M!=0 and (A*t+B*y)%M!=0:
            op+=1
print(op)
print(446*446)