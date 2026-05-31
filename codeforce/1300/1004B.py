import sys
#气笑了，奇偶交替始终是最优的
n,m = map(int,input().split())
if n%2==0:
    print('01'*(n//2))
else:
    print('01'*(n//2)+'0')

#0-rose,1-lily
#找出最大值
