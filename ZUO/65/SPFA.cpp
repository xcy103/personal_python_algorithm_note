// # Bellman-Ford + SPFA优化（Shortest Path Faster Algorithm）

// # 很轻易就能发现，每一轮考察所有的边看是否做松弛操作是不必要的
// # 因为只有上一次被某条边松弛过的节点，所连接的边，才有可能引起下一次的松弛操作
// # 所以用队列来维护“这一轮哪些节点的distance变小了”
// # 下一轮只需要对这些点的所有边，考察有没有松弛操作即可

// # SPFA只优化了常数时间，在大多数情况下跑得很快，但时间复杂度为O(n*m)
// # 看复杂度就知道只适用于小图，根据数据量谨慎使用，在没有负权边时要使用Dijkstra算法

// # 网上说，SPFA已死。有时候死了，有时候诈尸了，称为薛定谔的SPFA，这是什么意思？

// # Bellman-Ford + SPFA优化的用途

// # 1）适用于小图

// # 2）解决有负边（没有负环）的图的单源最短路径问题

// # 3）可以判断从某个点出发是否能遇到负环，如果想判断整张有向图有没有负环，需要设置虚拟源点

// # 4）并行计算时会有很大优势，因为每一轮多点判断松弛操作是相互独立的，可以交给多线程处理

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2001;
const int MAXM = 6001;
const int MAXQ = 4000001;

int head[MAXN];
int nxt[MAXM];
int to[MAXM];
int weight[MAXM];
int cnt;

// SPFA
int dist[MAXN];
int updateCnt[MAXN];
int q[MAXQ];
bool enter[MAXN];
int l,r;

void build(int n){
    cnt = 1;
    l = r = 0;
    for(int i=1;i<=n;i++){
        head[i] = 0;
        enter[i] = false;
        updateCnt[i] = 0;
        dist[i] = INT_MAX;
    }
}
void addEdge(int u, int v, int w) {
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}

bool spfa(int n){
    //固定从1出发
    dist[1] = 0;
    updateCnt[1]++;
    q[r++] = 1;
    enter[1] = true;

    while(l<r){
        int u = q[l++];
        enter[u] = false;

        for(int e=head[u];e;e=nxt[e]){
            int v = to[e];
            int w = weight[e];

            if(dist[u]!=INT_MAX&&dist[v]>dist[u]+w){
                dist[v] = dist[u]+w;
                if(!enter[v]){
                        if(++updateCnt[v]>n-1){
                        return true;
                    }
                    q[r++] = v;
                    enter[v] = true;
                }
            }
        }
    }
    return false;
}
int main(){
    int cases;
    cin>>cases;
    while(cases--){
        int n,m;
        cin>>n>>m;
        build(n);
        for(int i=0;i<m;i++){
            int u,v,w;
            cin>>u>>v>>w;
            if(w>=0){
                addEdge(u, v, w);
                addEdge(v, u, w);
            }else{
                addEdge(u, v, w);
            }
        }
        printf("%s\n", spfa(n) ? "YES" : "NO");    
    }
    return 0;
}
