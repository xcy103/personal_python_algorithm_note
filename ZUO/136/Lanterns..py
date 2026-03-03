import sys

input = sys.stdin.readline

MOD = 2008

def solve():
    n,m = map(int, input().split())
    n-=1
    arr = []
    for _ in range(m):
        s = input.strip()
        num = 0
        for j in range(n+1):
            if s[j]=='O':
                num|=1<<j
        arr.append(num)
    
    basis = [0]*(n+1)

    def insert(num):
        for i in range(n,-1,-1):
            if num>>i&1:
                if basis[i]==0:
                    basis[i] = num
                    return True
                num^=basis[i]
        return False
    
    size = 0
    for num in arr:
        if insert(num): size+=1
    
    print(pow(2,size,MOD))

if __name__ == '__main__':
    solve()