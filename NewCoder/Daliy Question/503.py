import sys
from math import comb
n,x = map(int,input().split())

i = 1
op = 0
while i*i<=x:
    op+=1
    i+=1

print(comb(op,n))