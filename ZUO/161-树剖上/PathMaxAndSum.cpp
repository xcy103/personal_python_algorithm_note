// 路径最大值与累加和，c++版
// 一共有n个节点，给定n-1条边，节点连成一棵树，每个节点给定权值
// 一共有m条操作，每种操作是如下3种类型中的一种
// 操作 CHANGE x y : x的权值修改为y
// 操作 QMAX x y   : x到y的路径上，打印节点值的最大值
// 操作 QSUM x y   : x到y的路径上，打印节点值的累加和
// 1 <= n <= 3 * 10^4
// 0 <= m <= 2 * 10^5
// -30000 <= 节点权值 <= +30000
// 测试链接 : https://www.luogu.com.cn/problem/P2590

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 30001;
using ll  = long long;
int n,m;
int arr[MAXN],head[MAXN],nxt[MAXN<<1],to[MAXN<<1],cntg;
//重链信息
int fa[MAXN],dep[MAXN],siz[MAXN],son[MAXN],top[MAXN],dfn[MAXN],seg[MAXN],cntd;
ll max_tree[MAXN<<2],sum_tree[MAXN<<2];

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
    max_tree[i] = max(max_tree[i<<1],max_tree[i<<1|1]);
    sum_tree[i] = sum_tree[i<<1]+sum_tree[i<<1|1];
}

void build(int l,int r,int i){
    if(l==r){
        max_tree[i] = arr[seg[l]];
        sum_tree[i] = arr[seg[l]];
    }
    else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        up(i);
    }
}
void update(int jobi,int jobv,int l,int r,int i){
    if(l==r){
        max_tree[i] = jobv;
        sum_tree[i] = jobv;
    }else{
        int mid = (l+r)>>1;
        if(jobi<=mid) update(jobi,jobv,l,mid,i<<1);
        else update(jobi,jobv,mid+1,r,i<<1|1);
        up(i);
    }
}
ll querySum(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && jobr>=r) return sum_tree[i];
    else{
        int mid = (l+r)>>1;
        ll ans = 0;
        if(jobl<=mid){
            ans += querySum(jobl, jobr, l, mid, i << 1);
        }
        if(jobr>mid){
            ans += querySum(jobl, jobr, mid+1, r, i << 1|1);

        }
        return ans;
    }
}
int queryMax(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && jobr>=r) return max_tree[i];
    else{
        int mid = (l+r)>>1;
        int ans = INT_MIN;
        if(jobl<=mid){
            ans = max(ans,queryMax(jobl, jobr, l, mid, i << 1));
        }
        if(jobr>mid){
            ans = max(ans,queryMax(jobl, jobr, mid+1, r, i << 1|1));

        }
        return ans;
    }
}
ll pathSum(int x,int y){
    ll ans = 0;
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            ans = (ans + querySum(dfn[top[y]],dfn[y],1,n,1));
            y = fa[top[y]];
        }else{
            ans = (ans + querySum(dfn[top[x]],dfn[x],1,n,1));
            x = fa[top[x]];
        }
    }
    ans = (ans + querySum(min(dfn[x], dfn[y]),max(dfn[x], dfn[y]),1,n,1));
    return ans;
}
int pathMax(int x,int y){
    int ans = INT_MIN;
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            ans = max(ans,queryMax(dfn[top[y]],dfn[y],1,n,1));
            y = fa[top[y]];
        }else{
            ans = max(ans,queryMax(dfn[top[x]],dfn[x],1,n,1));
            x = fa[top[x]];
        }
    }
    ans = max(ans,queryMax(min(dfn[x], dfn[y]),max(dfn[x], dfn[y]),1,n,1));
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n;
    for(int i=1,u,v;i<n;i++){
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    
    dfs1(1,0);
    dfs2(1,1);
    build(1,n,1);
    int q;
    cin>>q;
    for(int i=1;i<=q;i++){
        string op;
        int u,v;
        cin>>op;
        if(op=="CHANGE"){
            cin>>u>>v;
            arr[u] = v;
            update(dfn[u],v,1,n,1);
        }else if(op=="QMAX"){
            cin>>u>>v;
            cout<<pathMax(u,v)<<"\n";
        }else if(op=="QSUM"){
            cin>>u>>v;
            cout<<pathSum(u,v)<<"\n";
        }
    }

    return 0;
}