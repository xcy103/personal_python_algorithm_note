// 多重背包通过二进制分组转化成01背包(模版)
// 宝物筛选
// 一共有n种货物, 背包容量为t
// 每种货物的价值(v[i])、重量(w[i])、数量(c[i])都给出
// 请返回选择货物不超过背包容量的情况下，能得到的最大的价值
// 测试链接 : https://www.luogu.com.cn/problem/P1776
// 二进制分组的思想是，因为每一个物品有多个，如果一个一个枚举，
// 就是我们来到一个商品，枚举这个商品有1个，2个，3个。。按照题目的数据量会超时
// 现在我们可以对这个某一种物品的个数进行转换，比如这种商品有16个
// 我们可以把这16个划分为，1个，2个，4个，8个，然后剩下1个，这些虚拟新物品
// 总和恰好等于原来小商品的个数，然后就，这些商品其实就没有标号了，，就算全部选了
// 也不会超过原来的商品个数，这样就转换成了01背包

// 二进制拆分把多重背包的cnt拆成1,2,4,...的组合，将问题转化为01背包；
// 虽然某些数量可以用不同组合表示（存在重复路径），
// 但不会影响最大值结果，同时可以覆盖1~cnt所有情况且不会超过cnt，
// 从而将复杂度从O(n*t*cnt)降为O(n*t*log cnt)
/*
Author: yangka
Date: 2026-03-19 16:58:14
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1001;
const int MAXW = 40001;
using ll  = long long;

int v[MAXN],w[MAXN],dp[MAXW];

int n,t,m;

int compute(){
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=m;i++){
        for(int j=t;j>=w[i];j--){
            dp[j] = max(dp[j],dp[j-w[i]]+v[i]);
        }
    }
    return dp[t];
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    while(cin>>n>>t){
        int value,weight,cnt;
        cin >> value >> weight >> cnt;
        for(int k=1;k<=cnt;k<<1){
            v[++m] = k*value;
            w[m] = k*weight;
            cnt-=k;
        }
        if(cnt){
            v[++m] = cnt*value;
            w[m] = cnt*weight;
        }
    }
    cout << compute() << '\n';

    return 0;
}