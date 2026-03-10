#  Bellman-Ford算法，
# 解决可以有负权边但是不能有负环（保证最短路存在）的图，单源最短路算法。
#  松弛操作
#  假设源点为A，从A到任意点F的最短距离为distance[F]。
#  假设从点P出发某条边，去往点S，边权为W。
#  如果发现，distance[P] + W < distance[S]，
#  也就是通过该边可以让distance[S]变小，那么就说，P出发的这条边对点S进行了松弛操作。
#  Bellman-Ford过程
#  1，每一轮考察每条边，每条边都尝试进行松弛操作，那么若干点的distance会变小。
#  2，当某一轮发现不再有松弛操作出现时，算法停止。
#  Bellman-Ford算法时间复杂度
#  假设点的数量为N，边的数量为M，每一轮时间复杂度O(M)
#  最短路径存在的情况下，因为1次松弛操作会使1个点的最短路的边数+1
#  而从源点出发到任何点的最短路最多走过全部的n个点，所以松弛的轮数必然 <= n - 1
#  所以Bellman-Ford算法时间复杂度O(M*N)
#  重要推广：判断从某个点出发能不能到达负环
#  上面已经说了，如果从A出发存在最短路（没有负环），那么松弛的轮数必然 <= n - 1
#  而如果从A点出发到达一个负环，那么松弛操作显然会无休止地进行下去
#  所以，如果发现从A点出发，在第n轮时松弛操作依然存在，说明从A点出发能够到达一个负环

#https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#这道题不太一样。。因为中转和每次松弛操作之间的中转不太对应
#因为边的处理顺序是不固定的，意思就是题目是想，每一轮松弛，我到一个地方
#距离变得更小，原来的bf算法可能直接搞定了，因为会继承，所以我们要建立一个新表
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cur = [inf]*n
        cur[src] = 0

        for _ in range(k+1):
            nxt = cur.copy()

            for [a,b,w] in flights:
                
                if cur[a]!=inf:
                    nxt[b] = min(nxt[b],cur[a] + w)
            
            cur = nxt
        
        return cur[dst] if cur[dst]!=inf else -1