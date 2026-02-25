import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int,data[1:]))

    bit = [0]*(n+1)
    def update(i,v):
        while i<=n:
            bit[i] += v
            i += i&-i
    
    def query(i):
        res = 0
        while i>0:
            res += bit[i]
            i -= i&-i
        return res
    
    op = 0
    for i,x in enumerate(arr):
        op+=i - query(x)
        update(x,1)
    print(op)
if __name__ == "__main__":
    solve()
