// 攻略，C++版
// 一共有n个节点，给定n-1条边，所有节点连成一棵树，每个点给定点权
// 规定1号点是头，任何路径都必须从头开始，然后走到某个叶节点停止
// 路径上的点，点权的累加和，叫做这个路径的收益
// 给定数字k，你可以随意选出k条路径，所有路径经过的点，需要取并集，也就是去重
// 并集中的点，点权的累加和，叫做k条路径的收益
// 打印k条路径的收益最大值
// 1 <= n、k <= 2 * 10^5
// 所有点权都是int类型的正数
// 测试链接 : https://www.luogu.com.cn/problem/P10641
/*
Author: yangka
Date: 2026-03-21 20:33:21
*/
//思路就是最值钱剖分，最值钱的儿子
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 200001;

using ll  = long long;
int n,k,arr[MAXN];
// 链式前向星
int head[MAXN], nxt[MAXN<<1], to[MAXN<<1], cnt;
//长剖
int fa[MAXN],son[MAXN],top[MAXN];
ll money[MAXN],res[MAXN];
//建图
void addEdge(int u, int v) {
   nxt[++cnt] = head[u];
   to[cnt] = v;
   head[u] = cnt;
}
//收集儿子
void dfs1(int u,int f){
    fa[u] = f;
    // money[u] = arr[u]; 最好写在下面吧
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f) dfs1(v,u);
    }
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f){
            if(son[u]==0 || money[son[u]]<money[v]) son[u] = v;
        }
    }
    money[u]+=money[son[u]] + arr[u];
}
//收集top
void dfs2(int u,int t){
    top[u] = t;
    if(son[u]==0) return;
    dfs2(son[u],t);
    for (int e = head[u], v; e > 0; e = nxt[e]) {
        v = to[e];
        if (v != fa[u] && v != son[u]) {
            dfs2(v, v);
        }
    }
}
ll compute(){
    int l = 0;
    for(int i=1;i<=n;i++){
        if(top[i]==i){
            res[++l] = money[i]; 
        }
    }
    sort(res+1,res+1+l);
    ll ans = 0;
    for(int i=1,j=l;i<=k;i++,j--){
        ans+=res[j];
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>k;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    for(int i=1;i<n;i++){
        int u,v;
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs1(1,0);
    dfs2(1,1);
    cout<<compute()<<"\n";
    

    return 0;
}