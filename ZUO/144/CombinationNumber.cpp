// 组合数问题
// 组合公式c(i, j)，表示从i个物品中选出j个物品的方案数
// 如果该数值是k的整数倍，那么称(i, j)是一个合法对
// 给定具体的一组数字n和m，当i和j满足：0 <= i <= n，0 <= j <= min(i, m)
// 返回有多少合法对
// 一共有t组测试，所有测试的k都为同一个值
// 每组测试给定n和m，打印每组测试的答案
// 1 <= t <= 10^4
// 2 <= k <= 21
// 0 <= n、m <= 2000
// 测试链接 : https://www.luogu.com.cn/problem/P2822
//组合数modk + 二位前缀和
#include<bits/stdc++.h>
using namespace std;

const int MAXV = 2000;
const int MAXN = 2002;

int c[MAXN][MAXN],f[MAXN][MAXN],sumv[MAXN][MAXN];

int t,k,n,m;

void build(){
    for(int i=0;i<=MAXV;i++){
        c[i][0] = 1;
        for(int j=1;j<=i;j++){
            c[i][j] = (c[i-1][j] + c[i-1][j-1]) % k;
        }
    }

    for(int i=1;i<=MAXV;i++){
        for(int j=1;j<=i;j++){
            f[i][j] = (c[i][j]%k)==0;
        }
    }

    for(int i=2;i<=MAXV;i++){
        for(int j=1;j<=i;j++){
            sumv[i][j] = (sumv[i-1][j]+
                        sumv[i][j-1]-
                        sumv[i-1][j-1] + f[i][j]);
        }
        sumv[i][i+1] = sumv[i][i];
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>t>>k;
    build();

    while(t--){
        cin>>n>>m;
        if(m>n){
            cout<<sumv[n][n]<<endl;
        }else{
            cout<<sumv[n][m]<<endl;
        }
    }
    return 0;
}