// 边权转化为点权的模版题，C++版
// 一共有n个节点，给定n-1条边，节点连成一棵树，初始时所有边的权值为0
// 一共有m条操作，每条操作是如下2种类型中的一种
// 操作 P x y : x到y的路径上，每条边的权值增加1
// 操作 Q x y : x和y保证是直接连接的，查询他们之间的边权
// 1 <= n、m <= 10^5
// 测试链接 : https://www.luogu.com.cn/problem/P3038
/*
Author: yangka
Date: 2026-03-21 14:40:55
*/
//就是把边权转为点权，x-y有一条边，就把这个边的边权下放给dfn序号
//大的，然后继续重链剖分
// 树链剖分——边权转点权总结：

// 1. 问题：树上边权的修改/查询（子树或路径）
// 2. 技巧：把边权下放给更深的节点 → 转为点权
// 3. 整体：对树重新进行重链剖分
// 4. 单边操作：找到该边的下方节点，操作其点权
// 5. 子树操作：忽略子树根节点的点权
// 6. 路径操作：忽略LCA节点的点权

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100001;

using ll  = long long;
int n,m;
//建图
int head[MAXN],nxt[MAXN<<1],to[MAXN<<1],cntg;
//树剖
int fa[MAXN],dep[MAXN],siz[MAXN],son[MAXN],dfn[MAXN],seg[MAXN],top[MAXN],cntd;
//线段树
int addTag[MAXN<<2],sum[MAXN<<2];
void addEdge(int u, int v) {
   nxt[++cntg] = head[u];
   to[cntg] = v;
   head[u] = cntg;
}
void dfs1(int u, int f) {
   fa[u] = f;
   dep[u] = dep[f] + 1;
   siz[u] = 1;
   for (int e = head[u], v; e > 0; e = nxt[e]) {
       v = to[e];
       if (v != f) {
           dfs1(v, u);
       }
   }
   for (int e = head[u], v; e > 0; e = nxt[e]) {
       v = to[e];
       if (v != f) {
           siz[u] += siz[v];
           if (son[u] == 0 || siz[son[u]] < siz[v]) {
               son[u] = v;
           }
       }
   }
}
//自己写的dfs2
void dfs2(int u,int t){
    top[u] = t;
    dfn[u] = ++cntd;
    seg[cntd] = u;
    if(son[u]==0) return;
    dfs2(son[u],t);
    for(int e = head[u],v;e;e=nxt[e]){
        v = to[e];
        if(v!=fa[u]&&v!=son[u]) dfs2(v,v);
    }
}
void up(int i){
    sum[i] = (sum[i<<1] + sum[i<<1|1]);
}
void lazy(int i,int v,int len){
    sum[i]+=v*len;
    addTag[i]+=v;
}
void down(int i, int ln, int rn) {
   if (addTag[i] != 0) {
       lazy(i << 1, addTag[i], ln);
       lazy(i << 1 | 1, addTag[i], rn);
       addTag[i] = 0;
   }
}

void add(int jobl, int jobr, int jobv, int l, int r, int i) {
   if (jobl <= l && r <= jobr) {
       lazy(i, jobv, r - l + 1);
   } else {
       int mid = (l + r) >> 1;
       down(i, mid - l + 1, r - mid);
       if (jobl <= mid) {
           add(jobl, jobr, jobv, l, mid, i << 1);
       }
       if (jobr > mid) {
           add(jobl, jobr, jobv, mid + 1, r, i << 1 | 1);
       }
       up(i);
   }
}

int query(int jobi, int l, int r, int i) {
   if (l == r) {
       return sum[i];
   }
   int mid = (l + r) >> 1;
   down(i, mid - l + 1, r - mid);
   if (jobi <= mid) {
       return query(jobi, l, mid, i << 1);
   } else {
       return query(jobi, mid + 1, r, i << 1 | 1);
   }
}
void pathAdd(int x,int y,int v){
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            add(dfn[top[y]],dfn[y],v,1,n,1);
            y = fa[top[y]];
        }else{
            add(dfn[top[x]],dfn[x],v,1,n,1);
            x = fa[top[x]];
        }
    }
    add(min(dfn[x],dfn[y])+1,max(dfn[x],dfn[y]),v,1,n,1);
}
int edgeQuery(int x,int y){
    int low = max(dfn[x],dfn[y]);
    return query(low, 1, n, 1);
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>m;
    for(int i=1;i<n;i++){
        int u,v;
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs1(1,0);
    dfs2(1,1);
    char op;
    for(int i=1,x,y;i<=m;i++){
        cin>>op>>x>>y;
        if(op=='P'){
            pathAdd(x,y,1);
        }else{
            cout << edgeQuery(x, y) << "\n";
        }
    }

    return 0;
}