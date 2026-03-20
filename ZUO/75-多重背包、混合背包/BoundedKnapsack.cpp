// 多重背包不进行枚举优化
// 宝物筛选
// 一共有n种货物, 背包容量为t
// 每种货物的价值(v[i])、重量(w[i])、数量(c[i])都给出
// 请返回选择货物不超过背包容量的情况下，能得到的最大的价值
// 测试链接 : https://www.luogu.com.cn/problem/P1776
/*
Author: yangka
Date: 2026-03-19 16:28:28
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 101;
const int MAXW = 40001;
using ll  = long long;
int n,t;

int v[MAXN],w[MAXN],c[MAXN],dp[MAXW];
// 三维枚举（严格位置依赖）
int compute1(){
    vector<vector<int>> dp1(n + 1, vector<int>(t + 1, 0));
    for(int i=1;i<=n;i++){
        for(int j=0;j<=t;j++){
            dp1[i][j] = dp1[i-1][j];
            for(int k=1;k<=c[i]&&w[i]*k<=j;k++){
                dp1[i][j] = max(dp1[i][j],
                dp1[i][j-k*c[i]]+k*v[i]);
            }
        }
    }
    return dp1[n][t];
}
//空间压缩
int compute(){
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=n;i++){
        for(int j=t;j>=0;j--){
            for(int k=1;k<=c[i]&&k*w[i]<=j;k++){
                dp[j] = max(dp[j],
                dp[j-k*w[i]] + k*v[i]);
            }
        }
    }
    return dp[t];
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    while(cin>>n>>t){
        for(int i=1;i<=n;i++){
            cin >> v[i] >> w[i] >> c[i];
        }
        cout<<compute()<<"\n";
    }

    return 0;
}