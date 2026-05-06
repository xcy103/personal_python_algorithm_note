import sys
from itertools import pairwise
s = map(int,input().strip())

op = 1
for x,y in pairwise(s):
    if x!=y:
        op+=1
