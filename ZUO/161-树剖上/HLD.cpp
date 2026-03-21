// 重链剖分模版题，C++版
// 一共有n个节点，给定n-1条边，节点连成一棵树
// 给定每个节点的初始权值，给定树的头节点编号root
// 一共有m条操作，每种操作是如下4种类型中的一种
// 操作 1 x y v : x到y的路径上，每个节点值增加v
// 操作 2 x y   : x到y的路径上，打印所有节点值的累加和
// 操作 3 x v   : x为头的子树上，每个节点值增加v
// 操作 4 x     : x为头的子树上，打印所有节点值的累加和
// 1 <= n、m <= 10^5
// 1 <= MOD <= 2^30
// 输入的值都为int类型
// 查询操作时，打印(查询结果 % MOD)，题目会给定MOD值
// 测试链接 : https://www.luogu.com.cn/problem/P3384
// 树链剖分（HLD）

// 1. 每个节点信息：
// fa(父), dep(深度), siz(子树大小)
// son(重儿子=子树最大), top(重链头)
// dfn(时间戳), seg[dfn]=原节点

// 2. dfs1：
// 求 fa, dep, siz, son（不分配dfn）

// 3. dfs2：
// 先走重儿子 → 再走轻儿子
// 分配 dfn, top
// 重链上节点 top 相同，轻儿子开新链

// 4. 性质：
// 同一重链 dfn 连续
// 同一子树 dfn 连续

// 5. 子树操作：
// 转化为线段树区间操作

// 6. 路径操作：
// 拆成若干重链，逐段查询 + 合并

// 7. 复杂度：
// 路径查询 O(log^2 n)，子树查询 O(log n)

/*
Author: yangka
Date: 2026-03-20 14:23:37
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100001;
using ll  = long long;
int n,m,root,MOD;
int arr[MAXN],head[MAXN],nxt[MAXN<<1],to[MAXN<<1],cntg;
//重链信息
int fa[MAXN],dep[MAXN],siz[MAXN],son[MAXN],top[MAXN],dfn[MAXN],seg[MAXN],cntd;
ll sum[MAXN<<2],addTag[MAXN<<2];

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
//dfs2设置重链头，dfn序号，以及dfn与原始序号的对应
void dfs2(int u,int t){
    top[u] = t;
    dfn[u] = ++cntd;
    seg[cntd] = u;
    if(son[u] == 0) return;
    dfs2(son[u],t);
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=fa[u] && v!=son[u]){
            dfs2(v,v);//开始一个新的重链
        }
    }
}
void up(int i){
    sum[i] = (sum[i<<1]+sum[i<<1|1])%MOD;
}
void lazy(int i,ll v,int n){
    sum[i] = (sum[i]+v*n)%MOD;
    addTag[i] = (addTag[i] + v)%MOD;
}
void down(int i,int ln,int rn){
    if(addTag[i]){
        lazy(i<<1,addTag[i],ln);
        lazy(i<<1|1,addTag[i],rn);
        addTag[i] = 0;
    }
}
void build(int l,int r,int i){
    if(l==r) sum[i] = arr[seg[l]]%MOD;//注意这里是l，，不是他妈的i
    else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        up(i);
    }
}
void add(int jobl,int jobr,int jobv,int l,int r,int i){
    if(jobl<=l && jobr>=r) lazy(i,jobv,r-l+1);
    else{
        int mid = (l+r)>>1;
        down(i,mid-l+1,r-mid);
        if(jobl<=mid) add(jobl,jobr,jobv,l,mid,i<<1);
        if(jobr>mid) add(jobl,jobr,jobv,mid+1,r,i<<1|1);
        up(i);
    }
}
ll query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && jobr>=r) return sum[i];
    else{
        int mid = (l+r)>>1;
        down(i,mid-l+1,r-mid);
        ll ans = 0;
        if(jobl<=mid){
            ans = (ans + query(jobl, jobr, l, mid, i << 1))%MOD;
        }
        if(jobr>mid){
            ans = (ans + query(jobl, jobr, mid+1, r, i << 1|1))%MOD;

        }
        return ans;
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
    add(min(dfn[x], dfn[y]), max(dfn[x], dfn[y]), v, 1, n, 1);
}
void subtreeAdd(int x,int v){
    add(dfn[x],dfn[x]+siz[x]-1,v,1,n,1);
}
ll pathSum(int x,int y){
    ll ans = 0;
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            ans = (ans + query(dfn[top[y]],dfn[y],1,n,1))%MOD;
            y = fa[top[y]];
        }else{
            ans = (ans + query(dfn[top[x]],dfn[x],1,n,1))%MOD;
            x = fa[top[x]];
        }
    }
    ans = (ans + query(min(dfn[x], dfn[y]),max(dfn[x], dfn[y]),1,n,1))%MOD;
    return ans;
}
ll subtreeSum(int x){
    return query(dfn[x],dfn[x]+siz[x]-1,1,n,1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>m>>root>>MOD;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    for(int i=1,u,v;i<n;i++){
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs1(root,0);
    dfs2(root,root);
    build(1,n,1);
    for(int i=1,op,x,y,v;i<=m;i++){
        cin>>op;
        if(op==1){
            cin>>x>>y>>v;
            pathAdd(x,y,v);
        }else if(op==2){
            cin>>x>>y;
            cout << pathSum(x, y) << "\n";
        }else if(op==3){
            cin>>x>>v;
            subtreeAdd(x, v);
        }else{
            cin>>x;
            cout<<subtreeSum(x)<<"\n";
        }
    }

    return 0;
}