#起点确定了，之后的人也确定了，只需要走一遍然后判断是否合理
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    s = sum(a)
    if s % n:
        print("NO")
        continue
    
    t = s // n
    
    # 必要条件：每个只能是 t-1, t, t+1
    if any(abs(x - t) > 1 for x in a):
        print("NO")
        continue
    
    d = [t - x for x in a]
    
    def check(x0):
        x = x0
        for i in range(1, n):
            x -= d[i]
            if x not in (0, 1) or (a[i] == 0 and x == 1):
                return False
        return x0 == x - d[0]
    
    print("YES" if check(0) or check(1) else "NO")