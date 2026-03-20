// 购买足量干草的最小花费
// 有n个提供干草的公司，每个公司都有两个信息
// cost[i]代表购买1次产品需要花的钱
// val[i]代表购买1次产品所获得的干草数量
// 每个公司的产品都可以购买任意次
// 你一定要至少购买h数量的干草，返回最少要花多少钱
// 测试链接 : https://www.luogu.com.cn/problem/P2918
// 【方法1：最少花费】
// dp[i][j]：前i个公司，刚好j斤干草的最小花费
// 目标：≥h时最小cost

// 【方法2：最多干草】
// dp[i][j]：前i个公司，花费≤j时最多干草
// 目标：固定预算最大value

// 【核心区别】
// 方法1：定value→最小cost
// 方法2：定cost→最大value

// 【本题】
// 完全背包 + 至少装满 + 最小花费

// 【关键】
// m = h + max(val)
// 答案 = min(dp[h...m])
/*
Author: yangka
Date: 2026-03-19 15:30:17
*/
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 101;
const int MAXM = 55001;

int val[MAXN],cost[MAXN],dp[MAXM];
int n,h,maxv,m;

// dp[i][j] : 1...i里挑公司，购买严格j磅干草，需要的最少花费
// 1) dp[i-1][j]
// 2) dp[i][j-val[i]] + cost[i]
// 两种可能性中选最小
int compute2(){
    memset(dp,INT_MAX,sizeof(dp));
    // 初始化：dp[0] = 0，其余为无穷大
    dp[0] = 0;
    for(int i=1;i<=n;i++){
        for(int j=val[i];j<=m;j++){
            if(dp[j-val[i]]!=INT_MAX){
                dp[j] = min(dp[j], dp[j - val[i]] + cost[i]);
            }
        }
    }
    int ans = INT_MAX;
    for(int j=h;j<=m;j++){
        ans = min(ans,dp[j]);
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(cin>>n>>h){
        maxv = 0;
        for(int i=1;i<=n;i++){
            cin>>val[i]>>cost[i];
            maxv = max(maxv,val[i]);
        }
        m = h+maxv;
        cout<<compute2()<<"\n";
    }

    return 0;
}