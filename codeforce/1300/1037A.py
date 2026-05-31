import sys
from math import log2
n = int(input())

i = 0
while (1<<i)-1<n:
    i+=1
print(i)
