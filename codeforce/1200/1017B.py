import sys

n = int(input())
a = list(input())
b = list(input())

c1 = 0
zero = 0
c10 = 0
c01 = 0
for ch in a:
    if ch=='1':
        c1+=1
for i in range(n):
    if a[i]=='0' and b[i]=='0':
        zero+=1
    if a[i]=='1' and b[i]=='0':
        c10+=1
    if a[i]=='0' and b[i]=='1':
        c01+=1
print(c1*zero+c10*c01)