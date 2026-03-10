//最后两道题都是，分层图最短路加上dijsktra算法,上一题lc的旅行计划
//有点不同的分析是，分层图前进的话，如果充电，只充一格点。如果一次冲好多格，
//可能会丢失状态讨论
//还在这里学到了c++中利用结构体构建分层图最短路
/*
Author: yangka
Date: 2026-03-09 23:59:51
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 10001;
const int MAXM = 100001;
const int MAXK = 11;
using ll  = long long;
// 链式前向星
int head[MAXN], nxt[MAXM], to[MAXM], cnt;
int weight[MAXM];

int dist[MAXN][MAXK];
bool visited[MAXN][MAXK];
int n,m,k,s,t;

struct Node{
    int city;
    int use;
    int cost;
    bool operator < (const Node &a) const{
        return cost > a.cost;
    }
};
priority_queue<Node> heap;

void build(){
    cnt = 1;
    for(int i=0;i<n;i++){
        head[i] = 0;
        for(int j=0;j<=k;j++){
            dist[i][j] = INT_MAX;
            visited[i][j] = false;
        }
    }
    while(!heap.empty()) heap.pop();
}
void add_edge(int u,int v,int w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}
int dijkstra(){
    dist[s][0] = 0;
    heap.push({s,0,0});
    while(!heap.empty()){
        auto cur = heap.top();
        heap.pop();
        int city = cur.city;
        int use = cur.use;
        int cost = cur.cost;

        if(visited[city][use]) continue;
        visited[city][use] = true;
        if(city == t) return cost;

        for(int e = head[city];e;e = nxt[e]){
            int v = to[e];
            int w = weight[e];
            if(use<k&&dist[v][use+1]>cost){
                dist[v][use+1] = cost;
                heap.push({v,use+1,cost});
            }
            if(dist[v][use]>cost+w){
                dist[v][use] = cost+w;
                heap.push({v,use,cost+w});
            }
        }
    }
    return -1;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(cin>>n>>m>>k>>s>>t){
        build();

        for(int i=0;i<m;i++){
            int u,v,w;
            cin>>u>>v>>w;
            add_edge(u,v,w);
            add_edge(v,u,w);
        }
        cout<<dijkstra()<<endl;
    }

    return 0;
}