import sys
n,w,k = map(int,sys.stdin.readline().split())
L = []
for _ in range(k):
    L.append(int(sys.stdin.readline().strip()))
tree = [0]*(n+2)

for l in L:
    tree[l]+=1
    tree[l+w]-=1

for i in range(1,n+1):
    tree[i]+=tree[i-1]
print(*tree[1:-1])