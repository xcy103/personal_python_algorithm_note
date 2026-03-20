// 完全背包(模版)
// 给定一个正数t，表示背包的容量
// 有m种货物，每种货物可以选择任意个
// 每种货物都有体积costs[i]和价值values[i]
// 返回在不超过总容量的情况下，怎么挑选货物能达到价值最大
// 返回最大的价值
// 测试链接 : https://www.luogu.com.cn/problem/P1616
/*
Author: yangka
Date: 2026-03-19 13:43:26
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXM = 10001;
const int MAXT = 10000001;
using ll  = long long;
int cost[MAXM],val[MAXM];
ll dp[MAXT];

int t,m;
ll compute2(){
    for(int i=0;i<=t;i++) dp[i] = 0;

    for(int i=1;i<=m;i++){
        for(int j=cost[i];j<=t;j++){
            dp[j] = max(dp[j],dp[j-cost[i]] + val[i]);
        }
    }
    return dp[t];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(cin>>t>>m){
        for(int i=1;i<=m;i++){
            cin>>cost[i]>>val[i];
        }
        cout<<compute2()<<"\n";
    }

    return 0;
}