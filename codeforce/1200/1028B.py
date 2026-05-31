import sys

n,m = map(int,input().split())
#a全是9，b全是11111..01啥的
t = (n+8)//9
a = ['9']*t
b = ['9']*t+['0']*(t-1)+['1']
print(''.join(a))
print(''.join(b))