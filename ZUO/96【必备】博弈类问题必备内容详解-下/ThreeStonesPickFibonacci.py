#  三堆石头拿取斐波那契数博弈
#  有三堆石头，数量分别为a、b、c
#  两个人轮流拿，每次可以选择其中一堆石头，拿取斐波那契数的石头
#  拿到最后一颗石子的人获胜，根据a、b、c返回谁赢
#  来自真实大厂笔试，每堆石子的数量在10^5以内
#  没有在线测试，对数器验证

# 生成斐波那契
f = [1, 2]
while f[-1] + f[-2] <= 10**5:
    f.append(f[-1] + f[-2])

# 预处理SG（只做一次）
def build(mx):
    sg = [0] * (mx + 1)
    
    for i in range(1, mx + 1):
        appear = [False] * 30   # 关键优化,因为可操作的状态数目很少，只和fib数量有关
        
        for num in f:
            if num > i:
                break
            appear[sg[i - num]] = True
        
        for s in range(50):
            if not appear[s]:
                sg[i] = s
                break
    
    return sg


def win1(a, b, c):
    mx = max(a, b, c)
    sg = build(mx)
    return "先手" if (sg[a] ^ sg[b] ^ sg[c]) != 0 else "后手" 

