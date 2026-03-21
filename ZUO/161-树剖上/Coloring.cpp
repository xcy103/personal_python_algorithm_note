// 染色，C++版
// 一共有n个节点，给定n-1条边，节点连成一棵树，每个节点给定初始颜色值
// 连续相同颜色被认为是一段，变化了就认为是另一段
// 比如，112221，有三个颜色段，分别为 11、222、1
// 一共有m条操作，每种操作是如下2种类型中的一种
// 操作 C x y z : x到y的路径上，每个节点的颜色都改为z
// 操作 Q x y   : x到y的路径上，打印有几个颜色段
// 1 <= n、m <= 10^5
// 1 <= 任何时候的颜色值 <= 10^9
// 测试链接 : https://www.luogu.com.cn/problem/P2486
/*
Author: yangka
Date: 2026-03-20 16:37:12
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100001;

using ll  = long long;

int n,m,arr[MAXN],head[MAXN],nxt[MAXN<<1],to[MAXN<<1],cntg;
//树剖信息
int fa[MAXN],son[MAXN],dfn[MAXN],dep[MAXN],siz[MAXN],seg[MAXN],top[MAXN],cntd;
//线段树
int sum[MAXN<<2],lcolor[MAXN<<2],rcolor[MAXN<<2],change[MAXN<<2];

void addEdge(int u,int v){
    nxt[++cntg] = head[u];
    to[cntg] = v;
    head[u] = cntg;
}
//收集dep,siz,son,fa
void dfs1(int u,int f){
    fa[u] = f;
    dep[u] = dep[f]+1;
    siz[u] = 1;
    for(int e=head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f) dfs1(v,u);
    }
    for(int e=head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f){
            siz[u]+=siz[v];
            if(son[u]==0 || siz[son[u]]<siz[v]) son[u] = v;
        }
    }
}
//收集dfn,seg,top
void dfs2(int u,int t){
    top[u] = t;
    dfn[u] = ++cntd;
    seg[cntd] = u;
    if(son[u]==0) return;
    dfs2(son[u],t);
    for(int e=head[u],v;e;e = nxt[e]){
        v = to[e];
        //不是头节点，且不是重孩子
        if(v!=fa[u] && v!=son[u]) dfs2(v,v);
    }
}
void up(int i){
    sum[i] = sum[i<<1]+sum[i<<1|1];
    if(rcolor[i<<1]==lcolor[i<<1|1]) sum[i]--;
    rcolor[i] = rcolor[i<<1|1];//这里不要写错。。
    lcolor[i] = lcolor[i<<1];
}
void lazy(int i,int v){
    sum[i] = 1;
    lcolor[i] = v;
    rcolor[i] = v;
    change[i] = v;
}

void down(int i){
    if(change[i]){
        lazy(i<<1,change[i]);
        lazy(i<<1|1,change[i]);
        change[i] = 0;
    }
}
void build(int l,int r,int i){
    if(l==r){
        sum[i] = 1;
        lcolor[i] = arr[seg[l]];
        rcolor[i] = arr[seg[l]];
    }else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        up(i);
    }
}
void update(int jobl,int jobr,int jobv,int l,int r,int i){
    if(jobl<=l && jobr>=r) lazy(i,jobv);
    else{
        int mid = (l+r)>>1;
        down(i);
        if(jobl<=mid) update(jobl,jobr,jobv,l,mid,i<<1);
        if(jobr>mid) update(jobl,jobr,jobv,mid+1,r,i<<1|1);//总是这个写错
        up(i);
    }
}
int query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && jobr>=r) return sum[i];
    else{
        int mid = (l+r)>>1;
        down(i);
        if(jobr<=mid) return query(jobl,jobr,l,mid,i<<1);
        else if(jobl>mid) return query(jobl,jobr,mid+1,r,i<<1|1);//注意这里一定是左边界大于Mid
        else{
            int ans = query(jobl,jobr,l,mid,i<<1)+query(jobl,jobr,mid+1,r,i<<1|1);
            if(rcolor[i<<1]==lcolor[i<<1|1]) ans--;
            return ans;
        }
    }
}
int singleColor(int jobi,int l,int r,int i){
    if(l==r) return lcolor[i];
    down(i);
    int mid = (l+r)>>1;
    if(jobi<=mid) return singleColor(jobi,l,mid,i<<1);
    else return singleColor(jobi,mid+1,r,i<<1|1);

}
void pathUpdate(int x,int y,int v){
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            update(dfn[top[y]],dfn[y],v,1,n,1);
            y = fa[top[y]];
        }else{
            update(dfn[top[x]],dfn[x],v,1,n,1);
            x = fa[top[x]];
        }
    }

    update(min(dfn[x],dfn[y]),max(dfn[x],dfn[y]),v,1,n,1);         
}
int pathColors(int x,int y){
    int ans = 0,sonc,fac;
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            ans+=query(dfn[top[y]],dfn[y],1,n,1);
            sonc = singleColor(dfn[top[y]],1,n,1);
            
            fac = singleColor(dfn[fa[top[y]]],1,n,1);
            y = fa[top[y]];
            
        }else{
            ans+=query(dfn[top[x]],dfn[x],1,n,1);
            sonc = singleColor(dfn[top[x]],1,n,1);
            
            fac = singleColor(dfn[fa[top[x]]],1,n,1);
            x = fa[top[x]];
        }
        if(sonc==fac) ans--;
    }
    ans+=query(min(dfn[x], dfn[y]), max(dfn[x], dfn[y]), 1, n, 1);
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    for(int i=1,u,v;i<n;i++){
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs1(1,0);
    dfs2(1,1);
    build(1,n,1);
    string op;
    int x,y;
    for(int i=1;i<=m;i++){
        cin>>op;
        cin>>x>>y;
        if(op=="C"){
            int z;
            cin>>z;
            pathUpdate(x,y,z);
        }else{
            cout<<pathColors(x,y)<<"\n";
        }
    }
    return 0;
}