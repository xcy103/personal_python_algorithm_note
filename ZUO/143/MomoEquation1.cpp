/*
Author: yangka
Date: 2026-03-04 22:27:17
*/

#include <bits/stdc++.h>
using namespace std;

using ll  = long long;
using pli = pair<ll,int>;
using minpq = priority_queue<pli, vector<pli>, greater<pli>>;

const int MAXN = 500001;
const int MAXM = 5000001;

// 链式前向星
int head[MAXN], nxt[MAXM], to[MAXM], cnt;
ll weight[MAXM];
int n,x;
ll l,r;
ll dist[MAXN];
bool vis[MAXN];
minpq pq;
void add_edge(int u,int v,ll w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}

void prepare(){
    cnt = 1;
    while(!pq.empty())pq.pop();
    fill(head, head + x, 0);
    fill(dist, dist + x, LLONG_MAX);
    fill(vis, vis + x, false);
}

void dijkstra(){
    pq.push({0,0});
    dist[0] = 0;

    while(!pq.empty()){
        auto [d,u] = pq.top();
        pq.pop();
        if(vis[u])continue;
        vis[u] = true;
        for(int e = head[u]; e; e = nxt[e]){
            int v = to[e];
            if(!vis[v] && dist[v] > dist[u] + weight[e]){
                dist[v] = dist[u] + weight[e];
                pq.push({dist[v], v});
            }
        }

    }
}
ll compute(){
    dijkstra();
    ll ans = 0;
    for(int i=0;i<x;i++){
        if(r>=dist[i]) ans+=(r-dist[i])/x + 1;
        if(l>=dist[i]) ans-=(l-dist[i])/x + 1;
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>l>>r;
    l--;
    x = 0;
    for(int i=1;i<=n;i++){
        int v;
        cin>>v;
        if(v!=0){
            if(x==0){
                x = v;
                prepare();
            }else{
                for(int j=0;j<x;j++){
                    add_edge(j,(j+v)%x,v);
                }
            }
        }
    }
    cout<<compute()<<"\n";
    return 0;
}