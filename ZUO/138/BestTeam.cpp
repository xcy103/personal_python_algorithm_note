// 最佳团体
// 给定一棵树，节点编号0~n，0号节点是整棵树的头
// 编号1~n的节点，每个节点都有招募花费和战斗值，0号节点这两个值都是0
// 给定每条边(a,b)，表示节点a的父节点是b，有些节点的父节点是0节点
// 当招募了某个节点，那么该节点及其上方的所有祖先节点都需要招募
// 除了0号节点之外，一共可以招募k个人，希望让
// 战斗值之和 / 招募花费之和，这个比值尽量大，答案只需保留三位小数，更大的精度舍弃
// 1 <= k <= n <= 2500
// 0 <= 招募花费、战斗值 <= 10^4
// 测试链接 : https://www.luogu.com.cn/problem/P4322

#include<bits/stdc++.h>
using namespace std;

const int MAXN = 3001;
const int LIMIT = 10000;
const double NA = -1e9;
const double sml = 1e-6;
int head[MAXN],nxt[MAXN],to[MAXN],cnt;
//战斗花费
int cost[MAXN],power[MAXN];
//dfn
int dfn[MAXN],cntd,leafsize[MAXN];
double value[MAXN];
double dp[MAXN][MAXN];
int k,n;

void prepare(){
    for(int i = 0; i <= n; i++) head[i] = 0;
}
void addEdge(int u,int v){
    nxt[++cnt] = head[u];
    to[cnt] = v;
    head[u] = cnt;
}
int dfs(int u){
    int id = ++cntd;
    dfn[u] = id;
    leafsize[id] = 1;
    for(int e = head[u]; e; e = nxt[e]){
        int v = to[e];
        leafsize[u] += dfs(v);
    }
    return leafsize[id];
}
bool check(double x){
    for(int i = 0; i <= n; i++){
        value[dfn[i]] = (double)power[i] - cost[i] * x;
    }
    for(int j=1;j<=k;j++){
        dp[cntd+1][j] = NA;
    }
    for(int i=cntd;i>=2;i--){
        for(int j=1;j<=k;j++){
            dp[i][j] = max(
                dp[i+leafsize[i]][j],
                value[i] + dp[i+1][j-1]
            );
        }
    }
    return dp[2][k]>=0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>k>>n;
    prepare();

    for(int i=1;i<=n;i++){
        int p;
        cin>>cost[i]>>power[i]>>p;
        addEdge(p,i);
    }
    dfs(0);
    double l = 0,r = LIMIT;
    double ans = 0;
    while(l+sml<r){
        double mid = (l+r)/2;
        if(check(mid)){
            l = mid;
        }else{
            r = mid;
        }
    }
    printf("%.3f\n",l);
    return 0;
}