// 跳楼机
// 一座大楼一共有h层，楼层编号1~h，有如下四种移动方式
// 1, 向上移动x层
// 2, 向上移动y层
// 3, 向上移动z层
// 4, 回到1层
// 假设你正在第1层，请问大楼里有多少楼层你可以到达
// 1 <= h <= 2^63 - 1
// 1 <= x、y、z <= 10^5
// 测试链接 : https://www.luogu.com.cn/problem/P3403
#include<bits/stdc++.h>
using ll  = long long;
using pli = pair<ll,int>;
using minpq = priority_queue<pli, vector<pli>, greater<pli>>;
using namespace std;
const int MAXN = 100001;
const int MAXM = 200001;

ll h;
int x,y,z,head[MAXN],nxt[MAXM],to[MAXM],cnt;
ll weight[MAXM],dist[MAXN];
bool vis[MAXN];

void add_edge(int u,int v,ll w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>h>>x>>y>>z;
    h--;

    memset(head,0,sizeof(head));
    cnt = 1;
    for(int i=0;i<x;i++){
        add_edge(i,(i+y)%x,y);
        add_edge(i,(i+z)%x,z);
    }

    for(int i=0;i<x;i++){
        dist[i] = LLONG_MAX;
    }
    priority_queue<pair<ll,int> ,vector<pair<ll,int>>,greater<pair<ll,int>>> pq;
    dist[0] = 0;
    pq.push({0,0});

    while(!pq.empty()){
        auto [d,u] = pq.top();
        pq.pop();
        if(vis[u]) continue;
        vis[u] = true;
        for(int e=head[u];e;e=nxt[e]){
            int v = to[e];
            if(dist[v]>d+weight[e]){
                dist[v] = d+weight[e];
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

