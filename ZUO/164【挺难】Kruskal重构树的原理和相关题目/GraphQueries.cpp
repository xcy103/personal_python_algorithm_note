// 删边和查询，java版
// 图里有n个点，m条无向边，初始时点权都不同，图里可能有若干个连通的部分
// 一共有q条操作，每条操作是如下两种类型中的一种
// 操作 1 x : 点x所在的连通区域中，假设点y拥有最大的点权
//            打印y的点权，然后把y的点权修改为0
// 操作 2 x : 删掉第x条边
// 1 <= n <= 2 * 10^5    1 <= m <= 3 * 10^5    1 <= q <= 5 * 10^5
// 测试链接 : https://www.luogu.com.cn/problem/CF1416D
// 测试链接 : https://codeforces.com/problemset/problem/1416/D

#include<bits/stdc++.h>
using namespace std;

struct Edge{
    int u,v,w;
};
bool cmp(Edge x,Edge y){
    return x.w < y.w;
}

const int MAXN = 200001;
const int MAXK = 400001;
const int MAXM = 300001;
const int MAXQ = 500001;
const int MAXP = 20;
int n,m,q;
int node[MAXN];
Edge edge[MAXM];
int ques[MAXQ][2];
int f[MAXK],head[MAXK],nxt[MAXK],to[MAXK],cntg,cntu,nodeKey[MAXK];
int stjump[MAXK][MAXP],leafsize[MAXK],leafDfnMin[MAXK],leafseg[MAXK];
int cntd;
int maxValueDfn[MAXN<<2];

void prepare(){
    for(int i=1;i<=q;i++){
        if(ques[i][0]==2){
            edge[ques[i][1]].w = -1;
        }
    }
    int weight = 0;
    for(int i=1;i<=m;i++){
        if(edge[i].w!=-1){
            edge[i].w = ++weight;
        }
    }
    for(int i=q;i>=1;i--){
        if(ques[i][0]==2){
            edge[ques[i][1]].w = ++weight;
        }
    }
}
int find(int i) {
   if (i != f[i]) {
       f[i] = find(f[i]);
   }
   return f[i];
}

void addEdge(int u, int v) {
   nxt[++cntg] = head[u];
   to[cntg] = v;
   head[u] = cntg;
}

void kruskalRebuild(){
    for(int i=1;i<=n;i++){
        f[i] = i;
    }
    sort(edge+1,edge+m+1,cmp);
    cntu = n;
    for(int i=1,fx,fy;i<=m;i++){
        fx = find(edge[i].u);
        fy = find(edge[i].v);
        if(fx!=fy){
            f[fx] = f[fy] = ++cntu;
            f[cntu] = cntu;
            nodeKey[cntu] = edge[i].w;
            addEdge(cntu,fx);
            addEdge(cntu,fy);
        }
    }
}

void dfs(int u,int fa){
    stjump[u][0] = fa;
    for(int p=1;p<MAXP;p++){
        stjump[u][p] = stjump[stjump[u][p-1]][p-1];
    }
    for(int e = head[u];e;e = nxt[e]){
        dfs(to[e],u);
    }
    if(u<=n){
        leafsize[u] = 1;
        leafDfnMin[u] = ++cntd;
        leafseg[cntd] = u;
    }else{
        leafsize[u] = 0;
        leafDfnMin[u] = n+1;
    }
    for(int e = head[u];e;e = nxt[e]){
        leafsize[u] += leafsize[to[e]];
        leafDfnMin[u] = min(leafDfnMin[u], leafDfnMin[to[e]]);
    }
}

int getAncestor(int u,int limit){
    for(int p=MAXP-1;p>=0;p--){
        if(stjump[u][p] && nodeKey[stjump[u][p]]<=limit){
            u = stjump[u][p];
        }
    }
    return u;
}

void up(int i){
    int l = i<<1;
    int r = i<<1|1;
    if(node[leafseg[maxValueDfn[l]]]>node[leafseg[maxValueDfn[r]]]){
        maxValueDfn[i] = maxValueDfn[l];
    }else{
        maxValueDfn[i] = maxValueDfn[r];
    }
}
void build(int l,int r,int i){
    if(l==r){
        maxValueDfn[i] = l;
    }else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        up(i);
    }
}
void update(int jobi,int jobv,int l,int r,int i){
    if(l==r){
        node[leafseg[jobi]] = jobv;
    }else{
        int mid = (l+r)>>1;
        if(jobi<=mid){
            update(jobi,jobv,l,mid,i<<1);
        }else{
            update(jobi,jobv,mid+1,r,i<<1|1);
        }
        up(i);
    }
}
int query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && jobr>=r){
        return maxValueDfn[i];
    }else{
        int mid = (l+r)>>1;
        int ldfn = 0;
        int rdfn = 0;
        if(jobl<=mid){
            ldfn = query(jobl,jobr,l,mid,i<<1);
        }
        if(jobr>mid){
            rdfn = query(jobl,jobr,mid+1,r,i<<1|1);
        }
        return node[leafseg[ldfn]]>node[leafseg[rdfn]]?ldfn:rdfn;
    }
}

int queryAndupdate(int x,int limit){
    int anc = getAncestor(x,limit);
    int dfn = query(leafDfnMin[anc],leafDfnMin[anc]+leafsize[anc]-1,1,n,1);
    int ans = node[leafseg[dfn]];
    update(dfn,0,1,n,1);
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m>>q;
    for(int i=1;i<=n;i++){
        cin>>node[i];
    }
    for(int i=1;i<=m;i++){
        cin>>edge[i].u>>edge[i].v;
        edge[i].w = 0;
    }
    for(int i=1;i<=q;i++){
        cin>>ques[i][0]>>ques[i][1];
    }
    prepare();
    kruskalRebuild();
    for(int i=1;i<=cntu;i++){
        if(i==f[i]){
            dfs(i,0);
        }
    }
    build(1,n,1);
    int limit = m;
    for(int i=1;i<=q;i++){
        if(ques[i][0]==1){
            cout<<queryAndupdate(ques[i][1], limit)<<"\n";
        }else{
            limit--;
        }
    }
    return 0;

}