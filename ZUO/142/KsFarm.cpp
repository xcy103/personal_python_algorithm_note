#include<bits/stdc++.h>
using namespace std;

const int MAXN = 5001;
const int MAXM = 20001;
const int MAXQ = 200000001;

int head[MAXN],nxt[MAXM],to[MAXM],weight[MAXM],cnt;

int dist[MAXN],update[MAXN];
bool enter[MAXN];

int q[MAXQ],h,t;

int n,m;

void prepare(){
    h = t = 0;
    memset(head,0,sizeof(head));
    for(int i=0;i<=n;i++){
        dist[i] = INT_MAX;
        update[i] = 0;
        enter[i] = false;
    }
}

void add_edge(int u,int v,int w){
    nxt[++cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt;
}
bool spfa(int s){
    dist[s] = 0;
    update[s] = 1;
    q[t++] = s;
    enter[s] = true;

    while(h<t){
        int u = q[h++];
        enter[u] = false;
        for(int e=head[u];e;e=nxt[e]){
            int v = to[e];
            int w = weight[e];
            // if(dist[v]>dist[u] + w){
            //     dist[v] = dist[u] + w;
            //     if(!enter[v]){
            //         if(++update[v]>n){
            //             return true;
            //         }
            //         q[t++] = v;
            //         enter[v] = true;
            //     }
            // }
            //写在外面可以优化常数时间,不能这么写
            if(dist[v] > dist[u] + w){
                dist[v] = dist[u] + w;
                if(++update[v] > n){
                    return true;
                }
                if(!enter[v]){
                    q[t++] = v;
                    enter[v] = true;
                }
            }
        }
    }
    return false;
}

int main(){ 
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin>>n>>m;
    prepare();

    for(int i=1;i<=n;i++){
        add_edge(0,i,0);
    }
    for(int i=1;i<=m;i++){
        int type,u,v,w;
        cin>>type>>u>>v;
        if(type==1){
            cin>>w;
            add_edge(u,v,-w);
        }else if(type==2){
            cin>>w;
            add_edge(v,u,w);
        }else{
            add_edge(u,v,0);
            add_edge(v,u,0);
        }
    }
    if (spfa(0)) {
        cout << "No\n";
    } else {
        cout << "Yes\n";
    }

    return 0;
}
