// 选课，树上01背包的普通解法
// 在大学里每个学生，为了达到一定的学分，必须从很多课程里选择一些课程来学习
// 在课程里有些课程必须在某些课程之前学习，如高等数学总是在其它课程之前学习
// 现在有 N 门功课，每门课有个学分，每门课有一门或没有直接先修课
// 若课程 a 是课程 b 的先修课即只有学完了课程 a，才能学习课程 b
// 一个学生要从这些课程里选择 M 门课程学习
// 问他能获得的最大学分是多少
// 测试链接 : https://www.luogu.com.cn/problem/P2014
// 这道题的思路就是，有很多个课，然后课之间有依赖关系，
//如果你想上一门课必须把之前的先修课上了，可以画图理解，
//这里我们的思路是，创造一个虚拟节点，链接所有最开始的先修课，就是不需要任何先修课的课
//然后就是相当于，必须选我们这个虚拟节点然后再从子树上选一些节点
//并且可以串成链
/*
Author: yangka
Date: 2026-03-26 16:13:08
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 305;

int n,m,nums[MAXN];
// 链式前向星
int head[MAXN], nxt[MAXN], to[MAXN], cnt;
//dnf
int cntd,val[MAXN],sz[MAXN];
//dp
int dp[MAXN][MAXN];

void build(){
    memset(head, 0, sizeof(head));
    memset(dp, 0, sizeof(dp));
}
void add_edge(int u,int v){
    nxt[++cnt] = head[u];
    to[cnt] = v;
    head[u] = cnt;
}
// dfs拍平
int dfs(int u){
    int i = ++cntd;
    val[i] = nums[u];
    sz[i] = 1;
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        sz[i]+=dfs(v);
    }
    return sz[i];
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m;
    build();
    for(int i=1;i<=n;i++){
        int p;
        cin>>p>>nums[i];
        add_edge(p,i);
    }
    dfs(0);
    //核心dp
    for(int i=n+1;i>=2;i--){
        for(int j=1;j<=m;j++){
            dp[i][j] = max(dp[i+sz[i]][j],val[i]+dp[i+1][j-1]);
        }
    }
    cout << dp[2][m] << "\n";
    return 0;
}