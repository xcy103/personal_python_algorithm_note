#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 200005;
const int MAXM = MAXN<<1;

int head[MAXN],to[MAXM],nxt[MAXM],cnt;
ll weight[MAXN],dis[MAXN];
int MOD = 1000000007;
void addEdge(int u,int v,ll w){
    nxt[++cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt;
}

void dfs(int u,int fa){
    for(int e = head[u];e;e = nxt[e]){
        int v = to[e];
        if(v==fa) continue;
        dis[v] = dis[u]^weight[e];
        dfs(v,u);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        cnt = 0;
        for(int i=1;i<=n;i++){
            head[i] = 0;
            dis[i] = 0;
        }
        for(int i=1;i<n;i++){
            int u,v;
            ll w;
            cin>>u>>v>>w;
            addEdge(u,v,w);
            addEdge(v,u,w);
        }
        dfs(1,0);
        ll ans = 0;
        for(int bit = 0;bit<31;bit++){
            ll cnt1 = 0;
            ll cnt0 = 0;
            for(int i=1;i<=n;i++){
                if((dis[i]>>bit&1)){
                    cnt1++;
                }
                else{
                    cnt0++;
                }
            }
            ans = (ans + cnt1*cnt0*(1<<bit))%MOD;
        }
        cout<<ans<<"\n";
    }
    return 0;
    
}