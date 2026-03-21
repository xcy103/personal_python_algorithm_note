
// 重链剖分解决LCA查询，C++版
// 一共有n个节点，给定n-1条边，节点连成一棵树，给定头节点编号root
// 一共有m条查询，每条查询给定a和b，打印a和b的最低公共祖先
// 请用树链剖分的方式实现
// 1 <= n、m <= 5 * 10^5
// 测试链接 : https://www.luogu.com.cn/problem/P3379
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 500005;
using ll  = long long;
int n,m,root;
int arr[MAXN],head[MAXN],nxt[MAXN<<1],to[MAXN<<1],cntg;
//重链信息
int fa[MAXN],dep[MAXN],siz[MAXN],son[MAXN],top[MAXN];

void addEdge(int u,int v){
    nxt[++cntg] = head[u];
    to[cntg] = v;
    head[u] = cntg;
}
//dfs1设置父亲，子树大小，深度，重儿子
void dfs1(int u,int f){
    fa[u] = f;
    dep[u] = dep[f]+1;
    siz[u] = 1;
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f) dfs1(v,u);
    }
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f){
            siz[u]+=siz[v];
            if(son[u]==0 || siz[son[u]]<siz[v]){
                son[u] = v;
            }
        }
    }
}
int lca(int x,int y){
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            y = fa[top[y]];
        }else{
            x = fa[top[x]];
        }
    }
    return dep[y]<dep[x]?y:x;
}
//dfs2设置重链头
void dfs2(int u,int t){
    top[u] = t;
    if(son[u] == 0) return;
    dfs2(son[u],t);
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=fa[u] && v!=son[u]){
            dfs2(v,v);//开始一个新的重链
        }
    }
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>m>>root;
    for(int i=1;i<n;i++){
        int u,v;
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs1(root,0);
    dfs2(root,root);
    for(int i=1;i<=m;i++){
        int x,y;
        cin>>x>>y;
        cout<<lca(x,y)<<"\n";
    }

    return 0;
}