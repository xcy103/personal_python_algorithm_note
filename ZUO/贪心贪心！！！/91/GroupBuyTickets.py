#  组团买票
#  景区里一共有m个项目，景区的第i个项目有如下两个参数：
#  game[i] = { Ki, Bi }，Ki、Bi一定是正数
#  Ki代表折扣系数，Bi代表票价
#  举个例子 : Ki = 2, Bi = 10
#  如果只有1个人买票，单张门票的价格为 : Bi - Ki * 1 = 8
#  所以这1个人游玩该项目要花8元
#  如果有2个人买票，单张门票的价格为 : Bi - Ki * 2 = 6
#  所以这2个人游玩该项目要花6 * 2 = 12元
#  如果有5个人买票，单张门票的价格为 : Bi - Ki * 5 = 0
#  所以这5个人游玩该项目要花5 * 0 = 0元
#  如果有更多人买票，都认为花0元(因为让项目倒贴钱实在是太操蛋了)
#  于是可以认为，如果有x个人买票，单张门票的价格为 : Bi - Ki * x
#  x个人游玩这个项目的总花费是 : max { x * (Bi - Ki * x), 0 }
#  单位一共有n个人，每个人最多可以选1个项目来游玩，也可以不选任何项目
#  所有员工将在明晚提交选择，然后由你去按照上面的规则，统一花钱购票
#  你想知道自己需要准备多少钱，就可以应付所有可能的情况，返回这个最保险的钱数
#  数据量描述 : 
#  1 <= M、N、Ki、Bi <= 10^5
#  来自真实大厂笔试，没有在线测试，对数器验证

#这里有一种正难则反的贪心思想,先算出每个项目挣的钱，来一个人挣多少钱，再来一个人挣多少钱
#然后用大根堆组织，如果发现最挣钱的项目挣钱为－，就退出
#这里的挣钱是什么意思，就是来一个人需要给公园多少钱，压入的时候就是下一个人来需要给公园多少钱

import heapq

# 正式方法 O(n log m)
def enough2(n, games):
    # Python 默认是小根堆，所以用负值实现大根堆
    heap = []
    
    for k, b in games:
        game = [k, b, 0]  # ki, bi, people
        heapq.heappush(heap, (-earn(game), game))
    
    ans = 0
    
    for _ in range(n):
        if not heap:
            break
        
        e, game = heapq.heappop(heap)
        e = -e
        
        if e <= 0:
            break
        
        ans += e
        game[2] += 1  # people + 1
        
        heapq.heappush(heap, (-earn(game), game))
    
    return ans


def earn(game):
    k, b, people = game
    # 对应 Java 的公式
    return b - (people + 1) * k - people * k