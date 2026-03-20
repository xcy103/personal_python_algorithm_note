
// 分组背包(模版)
// 给定一个正数m表示背包的容量，有n个货物可供挑选
// 每个货物有自己的体积(容量消耗)、价值(获得收益)、组号(分组)
// 同一个组的物品只能挑选1件，所有挑选物品的体积总和不能超过背包容量
// 怎么挑选货物能达到价值最大，返回最大的价值
// 测试链接 : https://www.luogu.com.cn/problem/P1757
/*
Author: yangka
Date: 2026-03-19 12:51:43
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1001;
const int MAXM = 1001;
using ll  = long long;
// arr[i][0] 体积
// arr[i][1] 价值
// arr[i][2] 组号
// int arr[MAXN][3];

// int dp1[MAXM];
// int m,n;
// bool cmp(int a[], int b[]) {
//     return a[2] < b[2];
// }
//  ==========================
// 方法1：严格位置依赖 DP
// ==========================
// int compute1(){
//     int teams = 1;
//     for(int i=2;i<=n;i++){
//         if(arr[i-1][2]!=arr[i][2]) teams++;
//     }
//     vector<vector<int>> dp(teams+1,vector<int>(m+1,0));
//     for(int start = 1,end = 2,i = 1;start<=n;i++){
//         while(end<=n && arr[end][2]==arr[start][2]) end++;

//         当前组start ~ end -1
//         for(int j=0;j<=m;j++){
//             dp[i][j] = dp[i-1][j];
//             for(int k=start;k<end;k++){
//                 if(j>=arr[k][0]){
//                     dp[i][j] = max(dp[i][j],dp[i-1][j-arr[k][0]] + arr[k][1]);
//                 }
//             }
//         }
//         start = end++;
//     }
//     return dp[teams][m];
// }

//  ==========================
//  方法2：空间压缩，先遍历背包
//  ==========================
// int compute2(){
//     memset(dp1, 0, sizeof(dp1));
//     for(int start = 1,end = 2,i = 1;start<=n;i++){
//         while(end<=n && arr[start][2]==arr[end][2]) end++;

//         for(int j=m;j>=0;j--){
//             for(int k=start;k<end;k++){
//                 if(j>=arr[k][0]){
//                     dp1[j] = max(dp1[j-arr[k][0]] + arr[k][1],dp1[j]);
//                 }
//             }
//         }

//         start = end++;
//     }
//     return dp1[m];
// }
//  ==========================
//  方法3：空间压缩，先遍历物品 错误的。。这是分组背包，每一组内物品只能选一个
//  ==========================
//  int compute3(){
//      memset(dp1,0,sizeof(dp1));
//      for(int start = 1,end = 2,i=1;start<=n;i++){
//          while(end<=n && arr[start][2]==arr[end][2]) end++;

//          for(int k=start;k<end;k++){
//              for(int j=m;j>=arr[k][0];j--){
//                  dp1[j] = max(dp1[j],dp1[j-arr[k][0]] + arr[k][1]);
//              }
//          }
//          start = end++;
//      }
//      return dp1[m];
//  }
// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     while(cin>>m>>n){
//         for(int i=1;i<=n;i++){
//             cin>>arr[i][0]>>arr[i][1]>>arr[i][2];
//         }
//         这样写是错的。。
//         sort(arr + 1, arr + n + 1, [](const array<int,3>& a, const array<int,3>& b){
//             return a[2] < b[2];
//         });
//         cout<<compute1()<<"\n";
//         cout<<compute2()<<"\n";
//          cout<<compute3()<<"\n";
//     }

//     return 0;
// }
struct Node{
    int v,w,g;
}arr[MAXN];
int dp1[MAXM],n,m;
int compute2(){
    //空间压缩版本就可以不用统计组数了，因为不需要这一维度了
    memset(dp1,0,sizeof(dp1));
    for(int start = 1,end = 2,i = 1;start<=n;i++){
        while(end<=n && arr[start].g==arr[end].g) end++;

        for(int j=m;j>=0;j--){
            for(int k=start;k<end;k++){
                if(j>=arr[k].v){
                    dp1[j] = max(dp1[j],dp1[j-arr[k].v] + arr[k].w);
                }
            }
        }
        start = end++;
    }
    return dp1[m];
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    while(cin>>m>>n){
        for(int i=1;i<=n;i++){
            cin>>arr[i].v>>arr[i].w>>arr[i].g;
        }
    }
    sort(arr+1,arr+n+1,[](const Node& a,const Node& b){
        return a.g<b.g;
    });
    cout<<compute2()<<"\n";
    return 0;
}
