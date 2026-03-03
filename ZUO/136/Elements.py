import sys
input = sys.stdin.readline

BIT = 60

def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        state,power = map(int, input().split())
        arr.append((state,power))
    
    arr.sort(key=lambda x:-x[1])

    basis = [0]*(BIT+1)

    def insert(num):
        for i in range(BIT, -1, -1):
            if (num>>1)&1:
                if basis[i] == 0:
                    basis[i] = num
                    return True
                num^=basis[i]
        return False

    ans = 0
    for state,power in arr:
        if insert(state):
            ans+=power
    
    print(ans)

if __name__ == '__main__':
    solve()