// 多重背包单调队列优化
// 宝物筛选
// 一共有n种货物, 背包容量为t
// 每种货物的价值(v[i])、重量(w[i])、数量(c[i])都给出
// 请返回选择货物不超过背包容量的情况下，能得到的最大的价值
// 测试链接 : https://www.luogu.com.cn/problem/P1776
//下面的思路少了一点，需要根据余数分组
// 1️⃣ 原始转移
// dp[j] = max(dp[j - k*w] + k*v)   (0 <= k <= c)
// 瓶颈：O(n*t*c)
// -------------------------------------
// 2️⃣ 同余分组（关键）
// 按 j % w 分组：
// j, j-w, j-2w ... 一组
// -------------------------------------
// 3️⃣ 转换公式（核心）
// 令 x = j - k*w
// dp[j] = max(dp[x] + (j-x)/w * v)
//      = max(dp[x] - (x/w)*v) + (j/w)*v 注意做除法的时候，必须x/w或者j/w，因为同余分组
// 👉 优化目标：
// value(x) = dp[x] - (x/w)*v
// -------------------------------------
// 4️⃣ 单调队列（滑窗大小 = c+1）
// 维护 value(x) 最大值
// -------------------------------------
// 5️⃣ 倒序遍历（必须！）
// for (j = t - mod; j >= 0; j -= w)
// 原因：防止覆盖上一层 dp
// -------------------------------------
// 6️⃣ 每步三件事
// ① 入队（维护单调性）
// ② dp[j] = 队头 + (j/w)*v
// ③ 过期弹出
// -------------------------------------
// 7️⃣ 复杂度
// O(n * t)

#include <bits/stdc++.h>
using namespace std;

// 多重背包单调队列优化

const int MAXN = 101;
const int MAXW = 40001;

int v[MAXN],w[MAXN],c[MAXN],dp[MAXW],que[MAXW];
int l,r,n,t;

inline int value1(vector<vector<int>> &dp, int i, int j){
    return dp[i-1][j] - (j/w[i])*v[i];
}

int compute1(){
    vector<vector<int>> dp2(n + 1, vector<int>(t + 1, 0));
    for(int i=1;i<=n;i++){
        for(int mod = 0;mod<= min(t,w[i]-1);mod++){
            l = r = 0;
            for(int j=mod;j<=t;j+=w[i]){
                //单调队列里存的是下标
                while(l<r && value1(dp2,i,que[r-1])<=value1(dp2,i,j)){
                    r--;
                }
                que[r++] = j;
                if(que[l]==j-(c[i]+1)*w[i]) l++;

                dp2[i][j] = value1(dp2,i,que[l]) + (j/w[i])*v[i];
            }
        }
    }
    return dp2[n][t];
}

inline int value2(int i,int j){
    return dp[j] - (j/w[i])*v[i];
}

int compute2(){
    for(int i=1;i<=n;i++){
        for(int mod = 0;mod<=min(t,w[i]-1);mod++){
            l = r = 0;
            for(int j=t-mod,cnt=1;j>=0&&cnt<=c[i];j-=w[i],cnt++){
                while(l<r && value2(i,que[r-1])<=value2(i,j)) r--;

                que[r++] = j;
            }
            for(int j=t-mod,enter = j-w[i]*c[i];j>=0;j-=w[i],enter-=w[i]){
                if(enter>=0){
                    while(l<r && value2(i,que[r-1])<=value2(i,enter)) r--;     
                    que[r++] = enter;  
                }
                
                dp[j] = value2(i,que[l]) + (j/w[i])*v[i];
                if(que[l]==j) l++;
            }
        }
    }
    return dp[t];
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    while(cin>>n>>t){
        for(int i=1;i<=n;i++){
            cin >> v[i] >> w[i] >> c[i];
        }
        // 如果想用未压缩版本：
        // cout << compute1() << '\n';

        // 默认用压缩版本
        memset(dp, 0, sizeof(dp));
        cout << compute2() << '\n';
    }
    return 0;
}