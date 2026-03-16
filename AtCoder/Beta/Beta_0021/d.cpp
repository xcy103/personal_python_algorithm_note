//注意一下dj算法的cpp写法，最小堆，链式前向星类实现建图
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 50005;
const int MAXM = 200005;
const ll INF = 4e18;

struct Edge{
    int to,nxt;
    ll w;
}edge[MAXM];
int haed[MAXN],cnt;

void add(int u,int v,ll w){
    edge[++cnt] = {v,haed[u],w};
    haed[u] = cnt;
}

struct Node{
    int v;
    ll d;
    bool operator < (const Node &t) const{
        return d > t.d;
    }
};

ll dis[MAXN];
int n,m,k;
ll dijsktra(int s,int t){
    for(int i = 1;i <= n;i++) dis[i] = INF;
    dis[s] = 0;
    priority_queue<Node> q;
    q.push({s,0});
    while(!q.empty()){
        Node cur = q.top();
        q.pop();
        int u = cur.v;
        if(dis[u] < cur.d) continue;
        if(u==t) return cur.d;

        for(int i = haed[u];i;i = edge[i].nxt){
            int v = edge[i].to;
            ll w = edge[i].w;
            if(dis[v] > dis[u] + w){
                dis[v] = dis[u] + w;
                q.push({v,dis[v]});
            }
        }
    }
    return INF;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m>>k;
    for(int i=0;i<m;i++){
        int u,v;ll w;
        cin>>u>>v>>w;
        add(u,v,w);
        add(v,u,w);
    }
    vector<int> p(k);
    for(int i=0;i<k;i++) cin>>p[i];
    ll ans = 0;
    int cur = 1;
    for(int i=0;i<k;i++){
        ll d = dijsktra(cur,p[i]);
        if(d==INF){
            cout<<-1<<"\n";
            return 0;
        }
        ans += d;
        cur = p[i];
    }
    ll d = dijsktra(cur,n);
    if(d==INF){
        cout<<-1<<"\n";
        return 0;
    }
    ans += d;
    cout<<ans<<"\n";
    return 0;
}