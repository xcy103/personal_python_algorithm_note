def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    # 6k +/- 1 优化
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data: return
    T = int(input_data[0])
    
    for i in range(1, T + 1):
        x = int(input_data[i])
        
        # 0. 特殊情况
        if x <= 2:
            print(2)
            continue
        
        # 1. 寻找最近素数
        # 同时向两边扩散
        dist = 0
        while True:
            # 先查左边（因为等距取小，左边优先）
            if is_prime(x - dist):
                print(x - dist)
                break
            # 再查右边
            if is_prime(x + dist):
                print(x + dist)
                break
            dist += 1

# solve()