#这道题是差值比较，你可以先假设，所有人去a，然后计算出，a改到b，需要付出的代价，
#然后根据这个排序，挑选差值最小的前n个人，就是去b的，剩下的，由a改到b的代价很大的，
#就还是让他们去a
from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        t = len(costs)
        n = t//2
        costs.sort(key = lambda x:(x[0]-x[1]))
        res = 0
        for i in range(n):
            res+=costs[i][0]
        for i in range(n,t):
            res+=costs[i][1]
        return res