// 混合背包 + 多重背包普通窗口优化
// 能成功找零的钱数种类
// 每一种货币都给定面值val[i]，和拥有的数量cnt[i]
// 想知道目前拥有的货币，在钱数为1、2、3...m时
// 能找零成功的钱数有多少
// 也就是说当钱数的范围是1~m
// 返回这个范围上有多少可以找零成功的钱数
// 比如只有3元的货币，数量是5张
// m = 10
// 那么在1~10范围上，只有钱数是3、6、9时，可以成功找零
// 所以返回3表示有3种钱数可以找零成功
// 测试链接 : http://poj.org/problem?id=1742
// 这道题用了01背包，完全背包，和多重背包，对这三种背包的理解更加深刻了
// 01背包是，硬币只有一个。。（你说可能只有一个也超过吗，
// 完全背包是硬币数量x面值 超过，要兑换的最大的钱，
// 多重背包就是，数量多个，硬币数量x面值 未超过
/*
Author: yangka
Date: 2026-03-19 21:58:58
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 105;
const int MAXM = 100000 + 5;
using ll  = long long;

int val[MAXN],cnt[MAXN];
bool dp[MAXM];
int n,m;

int compute(){
    fill(dp+1,dp+m+1,false);
    dp[0] = true;
    for(int i=1;i<=n;i++){
        if(cnt[i]==1){
            for(int j=m;j>=val[i];j--){
                //dp[j] = dp[j-val[i]]; 注意，这里不能直接写，因为这里做了空间压缩
                //原来是，dp[i][j] = dp[i-1][j] || dp[i-1][j-val[i]] 这两种方案
                //的结合，你这样写就是直接的覆盖了，是不对的，下面也是
                if (dp[j - val[i]]) dp[j] = true;
            }
        }else if(cnt[i]*val[i]>m){
            for(int j=val[i];j<=m;j++){
                //dp[j] = dp[j - val[i]];
                if (dp[j - val[i]]) dp[j] = true;
            }
        }else{
            for(int mod = 0;mod<val[i];mod++){
                int c = 0;
                for(int j=m-mod,size=0;j>=0&&size<=cnt[i];j-=val[i],size++){
                    if(dp[j]) c++;
                }
                for(int j=m-mod,l=j-val[i]*(cnt[i]+1);j>=1;j-=val[i],l-=val[i]){
                    if(dp[j]) c--;
                    else{
                        if(c) dp[j] = true;
                    }
                    if(l>=0 && dp[l]) c++;
                }
            }
            
        }
    }
    int ans = 0;
    for(int i=1;i<=m;i++){
        if(dp[i]) ans++;
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(cin>>n>>m){
        if(n==0 && m==0) break;
        for(int i=1;i<=n;i++) cin>>val[i];
        for(int i=1;i<=n;i++) cin>>cnt[i];
        cout<<compute()<<"\n";
    }

    return 0;
}