#  威佐夫博弈(Wythoff Game)
#  有两堆石子，数量任意，可以不同，游戏开始由两个人轮流取石子
#  游戏规定，每次有两种不同的取法
#  1) 在任意的一堆中取走任意多的石子
#  2) 可以在两堆中同时取走相同数量的石子
#  最后把石子全部取完者为胜者
#  现在给出初始的两堆石子的数目，返回先手能不能获胜
#  测试链接 : https://www.luogu.com.cn/problem/P2252

import sys
from decimal import Decimal, getcontext

# 提高精度（必须！否则会WA）
getcontext().prec = 30

# 黄金分割比例
split = Decimal("1.61803398874989484")

def compute(a, b):
    mn = min(a, b)
    mx = max(a, b)
    
    # 计算 floor((mx - mn) * φ)
    k = mx - mn
    t = int((split * Decimal(k)))
    
    # 判断是否是奇异局面
    if mn != t:
        return 1
    else:
        return 0

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    
    res = []
    for a, b in zip(it, it):
        a = int(a)
        b = int(b)
        res.append(str(compute(a, b)))
    
    print("\n".join(res))

if __name__ == "__main__":
    main()