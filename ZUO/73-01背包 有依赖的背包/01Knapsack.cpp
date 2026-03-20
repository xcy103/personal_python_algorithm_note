// 01背包(模版)
// 给定一个正数t，表示背包的容量
// 有m个货物，每个货物可以选择一次
// 每个货物有自己的体积costs[i]和价值values[i]
// 返回在不超过总容量的情况下，怎么挑选货物能达到价值最大
// 返回最大的价值
// 测试链接 : https://www.luogu.com.cn/problem/P1048
//  每个物品可以选多次，就是多重背包，如果可以选无数次，就是完全背包
//  这里的dp定义为，前i物品，容量不超过j的情况下，所能选出的最大价值
//  由此可见这里的j，或者i不能太大
// dp[i][j] 表示：
// 前 i 个物品中自由选择，在容量不超过 j 的情况下的最大价值

// 其中：
// cost[i] 表示第 i 个物品的体积
// val[i]  表示第 i 个物品的价值

// 状态转移：

// 1) 不选第 i 个物品：
// dp[i][j] = dp[i-1][j]

// 2) 选第 i 个物品（前提 j >= cost[i]）：
// dp[i][j] = dp[i-1][j - cost[i]] + val[i]

// 综上：
// dp[i][j] = max(
//     dp[i-1][j],
//     dp[i-1][j - cost[i]] + val[i]   (j >= cost[i])
// )
#include<bits/stdc++.h>
using namespace std;

const int MAXM = 101;
const int MAXT = 1001;

int cost[MAXM],val[MAXM],dp[MAXT];
int t,n;

//这里的空间压缩，选择了从右向左更新，和dp的依赖有关
int compute2(){
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=n;i++){
        for(int j=t;j>=cost[i];j--){
            dp[j] = max(dp[j],dp[j-cost[i]] + val[i]);
        }
        return dp[t];
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    while(cin>>t>>n){
        for(int i=1;i<=n;i++){
            cin>>cost[i]>>val[i];
        }
        cout<<compute2()<<"\n";
    }
    return 0;
}