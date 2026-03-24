// 边的最大编号的最小值，C++版
// 图里有n个点，m条无向边，边的编号1~m，没有边权，所有点都连通
// 一共有q条查询，查询的格式如下
// 查询 x y z : 从两个点x和y出发，希望经过的点数量等于z
//              每个点可以重复经过，但是重复经过只计算一次
//              经过边的最大编号，最小是多少
// 3 <= n、m、q <= 10^5
// 3 <= z <= n
// 测试链接 : https://www.luogu.com.cn/problem/AT_agc002_d
// 测试链接 : https://atcoder.jp/contests/agc002/tasks/agc002_d

#include<bits/stdc++.h>
using namespace std;

struct Edge{
    int u,v,w;
};

bool cmp(Edge x,Edge y){
    return x.w<y.w;
}

const int MAXK = 200001;
const int MAXM = 100001;
const int MAXP = 20;
int n,m,q, f[MAXK],head[MAXK],nxt[MAXK],to[MAXK];
Edge edge[MAXM];
int cntg,cntu,leafsize[MAXK],stjump[MAXK][MAXP];
int nodeKey[MAXK];

void addEdge(int u,int v){
    nxt[++cntg] = head[u];
    to[cntg] = v;
    head[u] = cntg;
}

int find(int i) {
   if (i != f[i]) {
       f[i] = find(f[i]);
   }
   return f[i];
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
    if(u<=n) leafsize[u] = 1;
    else leafsize[u] = 0;

    for(int e = head[u];e;e = nxt[e]){
        leafsize[u]+=leafsize[to[e]];
    }
}
bool check(int x,int y,int z,int limit){
    for(int p=MAXP-1;p>=0;p--){
        if(stjump[x][p] && nodeKey[stjump[x][p]]<=limit){
            x = stjump[x][p];
        }
    }
    for(int p=MAXP-1;p>=0;p--){
        if(stjump[y][p] && nodeKey[stjump[y][p]]<=limit){
            y = stjump[y][p];
        }
    }
    if(x==y) return leafsize[x]>=z;
    else return leafsize[x] + leafsize[y] >= z;
}

int query(int x,int y,int z){
    int l = 0,r = m+1, ans = 0;
    while(l+1<r){
        int mid = (l+r)>>1;
        if(check(x,y,z,mid)) r = mid;
        else l = mid;
    }
    return r;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m;

    for(int i=1;i<=m;i++){
        cin >> edge[i].u >> edge[i].v;
        edge[i].w = i;
    }
    kruskalRebuild();
    dfs(cntu,0);
    cin>>q;
    for(int i=1;i<=q;i++){
        int x,y,z;
        cin>>x>>y>>z;
        cout << query(x, y, z) << "\n";
    }
    return 0;
}