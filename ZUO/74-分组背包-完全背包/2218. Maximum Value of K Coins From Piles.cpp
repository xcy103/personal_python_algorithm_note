// 从栈中取出K个硬币的最大面值和
// 一张桌子上总共有 n 个硬币 栈 。每个栈有 正整数 个带面值的硬币
// 每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里
// 给你一个列表 piles ，其中 piles[i] 是一个整数数组
// 分别表示第 i 个栈里 从顶到底 的硬币面值。同时给你一个正整数 m
// 请你返回在 恰好 进行 m 次操作的前提下，你钱包里硬币面值之和 最大为多少
// 测试链接 : https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
// 把每种方案，转为分组背包，每次只能挑选一个方案
//分组背包需要先遍历体积容量，然后再遍历物品
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxValueOfCoins2(vector<vector<int>>& piles, int m) {
        vector<int> dp(m+1);

        for(auto& team:piles){
            int t = min((int)team.size(),m);

            vector<int> pre(t+1,0);

            for(int j=0;j<t;j++){
                pre[j+1] = pre[j]+team[j];
            }
            for(int j=m;j>=0;j--){
                for(int k=1;k<=min(t,j);k++){
                    dp[j] = max(dp[j],dp[j-k]+pre[k]);
                }
            }
        }
        return dp[m];
    }
}