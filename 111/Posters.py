# 这道题考察并查集以及线段树的down操作
# 最后只查询一次，查线段树最后有多少个不同颜色

import sys

n,m = map(int,sys.stdin.readline().split())

pl = [0]*m
pr = [0]*m
coords = [n]

for i in range(m):
    pl[i],pr[i] = map(int,sys.stdin.readline().split())
    coords.append(pl[i])
    coords.append(pr[i])


coords.sort()


unique_coords = []
unique_coords.append(coords[0])
for i in range(1, len(coords)):
    if coords[i] != coords[i-1]:
        unique_coords.append(coords[i])

all_points = []
all_points.append(unique_coords[0])
for i in range(1, len(unique_coords)):
    if unique_coords[i] - unique_coords[i-1] > 1:
        all_points.append(unique_coords[i-1] + 1)
    all_points.append(unique_coords[i])
all_points.sort()

val_to_rank = {val:i+1 for i,val in enumerate(all_points)}
size = len(all_points)

tree_poster = [0]*(size<<2)

def down(i):
    if tree_poster[i] != 0:
        tree_poster[i << 1] = tree_poster[i]
        tree_poster[i << 1 | 1] = tree_poster[i]
        tree_poster[i] = 0

def update(jobl, jobr, jobv, l, r, i):
    if jobl <= l and r <= jobr:
        tree_poster[i] = jobv
        return
    down(i)
    mid = (l+r)>>1
    if jobl <= mid:
            update(jobl, jobr, jobv, l, mid, i << 1)
    if jobr > mid:
        update(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
    
visited = [False] * (m + 1)
visible_count = 0
def query(l,r,i):
    if tree_poster[i] != 0:
        p_id = tree_poster[i]
        global visible_count
        if not visited[p_id]:
            visited[p_id] = True
            visible_count += 1
        return
    if l==r:
        return 
    down(i)
    mid = (l + r) >> 1
    query(l, mid, i << 1)
    query(mid + 1, r, i << 1 | 1)

for i in range(m):
        update(val_to_rank[pl[i]], val_to_rank[pr[i]], i+1, 1, size, 1)

query(1, size, 1)
    
sys.stdout.write(str(visible_count) + "\n")