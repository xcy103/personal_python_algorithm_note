// 归程，C++版
// 一共有n个点，m条无向边，原图连通，每条边有长度l和海拔a
// 一共有q条查询，格式如下
// 查询 x y : 起初走过海拔 > y的边免费，可视为开车，但是车不能走海拔 <= y的边
//            你可以在任意节点下车，车不能再用
//            下车后经过每条边的长度(包括海拔 > y 的边)，都算入步行长度
//            你想从点x到1号点，打印最小步行长度
// 1 <= n <= 2 * 10^5
// 1 <= m、q <= 4 * 10^5
// 本题要求强制在线，具体规定请打开测试链接查看
// 测试链接 : https://www.luogu.com.cn/problem/P4768

#include <bits/stdc++.h>
using namespace std;

struct Edge{
    int u,v,l,a;
};
bool Edgecmp(Edge x, Edge y){
    return x.a > y.a;
}
struct HeapNode{
    int cur,dis;
};

struct HeapNodeCmp{
    bool operator()(const HeapNode& x,const HeapNode& y) const{
        return x.dis > y.dis;
    }
};

const int MAXN = 200001;
const int MAXK = 400001;
const int MAXM = 400001;
const int MAXP = 20;
int INF = 2000000001;
int t, n, m, q, k, s;
Edge edge[MAXM];
int headg[MAXN],nxtg[MAXM<<1],tog[MAXM<<1],weightg[MAXM<<1],cntg;
int dist[MAXN];
bool vis[MAXN];
priority_queue<HeapNode,vector<HeapNode>,HeapNodeCmp> heap;

int f[MAXK],headk[MAXK],nxtk[MAXK],tok[MAXK];
int cntk,nodeKey[MAXK],cntu;

int mindist[MAXK],stjump[MAXK][MAXP];

void clear(){
    cntg = 0,cntk = 0;
    for(int i=1;i<=n;i++){
        headg[i] = 0;
    }
    for(int i=1;i<=2*n;i++){
        headk[i] = 0;
    }
}
void addEdgeG(int u, int v, int w) {
   nxtg[++cntg] = headg[u];
   tog[cntg] = v;
   weightg[cntg] = w;
   headg[u] = cntg;
}

void dijkstra(){
    for(int i=1;i<=m;i++){
        addEdgeG(edge[i].u, edge[i].v, edge[i].l);
        addEdgeG(edge[i].v, edge[i].u, edge[i].l);
    }
    for(int i=1;i<=n;i++){
        dist[i] = INF;
        vis[i] = false;
    }
    dist[1] = 0;
    heap.push({1,0});
    int x,v;
    HeapNode node;
    while(!heap.empty()){
        node = heap.top();
        heap.pop();
        x = node.cur;
        v = node.dis;
        if(dist[x] < v) continue;

        for(int e = headg[x],y,w;e;e = nxtg[e]){
            y = tog[e];
            w = weightg[e];
            if(dist[y]>w+v){
                dist[y] = v + w;
                heap.push({y,dist[y]});
            }
        }
    }
}

void addEdgeK(int u, int v) {
   nxtk[++cntk] = headk[u];
   tok[cntk] = v;
   headk[u] = cntk;
}
int find(int i) {
   if(f[i] != i) {
       f[i] = find(f[i]);
   }
   return f[i];
}

void kruskalRebuild(){
    for(int i=1;i<=n;i++){
        f[i] = i;
    }
    sort(edge+1,edge+m+1,Edgecmp);

    cntu = n;
    for(int i=1,fx,fy;i<=m;i++){
        fx = find(edge[i].u);
        fy = find(edge[i].v);
        if(fx!=fy){
            f[fx] = f[fy] = ++cntu;
            f[cntu] = cntu;
            nodeKey[cntu] = edge[i].a;
            addEdgeK(cntu, fx);
            addEdgeK(cntu, fy);
        }
    }
}

void dfs(int u,int fa){
    stjump[u][0] = fa;
    for(int p = 1;p<MAXP;p++){
        stjump[u][p] = stjump[stjump[u][p-1]][p-1];
    }
    for(int e=headk[u];e;e = nxtk[e]){
        dfs(tok[e],u);
    }
    if(u<=n) mindist[u] = dist[u];
    else mindist[u] =INF;

    for(int e=headk[u];e;e = nxtk[e]){
        mindist[u] = min(mindist[u],mindist[tok[e]]);
    }

}

int query(int node,int line){
    for(int p = MAXP-1;p>=0;p--){
        if(stjump[node][p] && nodeKey[stjump[node][p]] > line){
            node = stjump[node][p];
        }
    }
    return mindist[node];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>t;
    for(int test = 1;test<=t;test++){
        cin>>n>>m;
        clear();
        for(int i=1;i<=m;i++){
            cin >> edge[i].u >> edge[i].v >> edge[i].l >> edge[i].a;
        }
        dijkstra();
        kruskalRebuild();
        dfs(cntu,0);
        cin>>q>>k>>s;
        for(int i=1,x,y,lastAns=0;i<=q;i++){
            cin>>x>>y;
            x = (x + k * lastAns - 1) % n + 1;
            y = (y + k * lastAns) % (s + 1);
            lastAns = query(x,y);
            cout << lastAns << "\n";
        }
    }
    return 0;
}