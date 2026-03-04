#include<bits/stdc++.h>
using namespace std;

const int MAXN = 1001;
const int MAXM = 20001;
const int MAXQ = 1000001;

int head[MAXN],nxt[MAXM],to[MAXM],weight[MAXM],cnt;

int dist[MAXN],update[MAXN];
bool enter[MAXN];
int q[MAXQ],h,t;

int n,m1,m2;

void prepare(){
    cnt = 1;
    memset(head,0,sizeof(head));
}

void add_edge(int u,int v,int w){ 
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}   
int spfa(int s){
    h = t = 0;
    for(int i=0;i<=n;i++){
        dist[i] = INT_MAX;
        update[i] = 0;
        enter[i] = false;
    }
    dist[s] = 0;
    update[s] = 1;
    enter[s] = true;
    q[t++] = s;
    while(h<t){
        int u = q[h++];
        enter[u] = false;
        for(int e=head[u];e;e=nxt[e]){
            int v = to[e];
            int w = weight[e];
            if(dist[v]>dist[u]+w){
                dist[v] = dist[u] + w;
                if(++update[v]>n) return -1;
                if(!enter[v]){
                    q[t++] = v;
                    enter[v] = true;
                }
            }
        }
    }
    if(dist[n] == INT_MAX) return -2;
    return dist[n];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m1>>m2;

    prepare();
    for(int i=1;i<=n;i++){
        add_edge(0,i,0);
    }

    for(int i=1;i<=m1;i++){
        int u,v,w;
        cin>>u>>v>>w;
        add_edge(u,v,w);
    }
    for(int i=1;i<=m2;i++){
        int u,v,w;
        cin>>u>>v>>w;
        add_edge(v,u,-w);
    }
    for(int i=1;i<n;i++){
        add_edge(i+1,i,0);
    }
    int ans = spfa(0);
    if(ans == -1){
        cout<<ans<<"\n";
    }else{
        ans = spfa(1);
        cout<<ans<<"\n";
    }
    return 0;

}