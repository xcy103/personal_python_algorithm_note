import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.fa = list(range(n+1))
    
    def find(self, x):
        while self.fa[x]!=x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return self.fa[x]
    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.fa[fa] = fb

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    
    dsu = DSU(n)
    
    # 建图（连边）
    for i in range(1, n+1):
        if i + x <= n:
            dsu.union(i, i + x)
        if i + y <= n:
            dsu.union(i, i + y)
    
    ok = True
    
    # 检查是否能排序
    for i in range(1, n+1):
        if dsu.find(i) != dsu.find(p[i]):
            ok = False
            break
    
    print("Yes" if ok else "No")