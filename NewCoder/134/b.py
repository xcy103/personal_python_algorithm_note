import sys

a,b,c,x,y = list(map(int,input().split()))

while c>=x or b>=y:
    if c>=x:
        b+=c//x
        c%=x
    if b>=y:
        a+=b//y
        c+=b//y
        b%=y
print(a)