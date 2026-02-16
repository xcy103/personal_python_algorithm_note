import sys

data = sys.stdin.read().split()
n,m = int(data[0]),int(data[1])
ptr = 2
intervals = []
for i in range(m):
    l,r = int(data[ptr]),int(data[ptr+1])
    ptr+=2
    intervals.append((l,r))
    

