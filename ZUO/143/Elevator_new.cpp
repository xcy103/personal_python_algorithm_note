#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 100001;
const int MAXM = 200001;

ll h,weight[MAXM],dist[MAXN];
int x,y,z,head[MAXN],nxt[MAXM],to[MAXM],cnt;
bool vis[MAXN];
struct Node{
    ll d;
    int u;
    bool operator < (const Node &rhs) const{
        return d > rhs.d;
    }
};
void add(int u,int v,ll w){
    nxt[++cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>h>>x>>y>>z;
    h--;

    memset(head,0,sizeof(head));
    for(int i=0;i<x;i++){
        add(i,(i+y)%x,y);
        add(i,(i+z)%x,z);
    }
    for(int i=0;i<x;i++){
        dist[i] = LLONG_MAX;
    }
    priority_queue<Node> pq;
    dist[0] = 0;
    pq.push({0,0});
    while(!pq.empty()){
        Node cur = pq.top();
        pq.pop();

        ll d = cur.d;
        int u = cur.u;
        if(dist[u] < d) continue;
        for(int e = head[u];e;e = nxt[e]){
            int v = to[e];
            ll w = weight[e];
            if(dist[v] > d + w){
                dist[v] = d + w;
                pq.push({dist[v],v});
            }
        }
    }
    ll ans = 0;
    for(int i=0;i<x;i++){
        if(dist[i]<=h){
            ans+=(h-dist[i])/x + 1;
        }
    }
    cout<<ans<<"\n";
    return 0;
}