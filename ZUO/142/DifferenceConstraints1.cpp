// 负环和差分约束模版题(转化成形式1进而转化成判断负环)
// 一共有n个变量，编号1~n，给定m个不等式，每个不等式的形式为
// Xi - Xj <= Ci，其中Xi和Xj为变量，Ci为常量
// 如果不等式存在矛盾导致无解，打印"NO"
// 如果有解，打印满足所有不等式的其中一组解(X1, X2...)
// 1 <= n、m <= 5 * 10^3
// -10^4 <= Ci <= +10^4 
// 测试链接 : https://www.luogu.com.cn/problem/P5960

#include<bits/stdc++.h>
using namespace std;

const int MAXN = 5001;
const int MAXM = 10001;
const int MAXQ = 5000001;

int head[MAXN],nxt[MAXM],to[MAXM],weight[MAXM],cnt;

int dist[MAXN],update[MAXN];
int q[MAXQ],h,t;

bool enter[MAXN];

int n,m;

void prepare(){
    cnt = 1;
    h = t =0;
    for(int i=0;i<=n;i++){
        head[i] = 0;
        dist[i] = INT_MAX;
        update[i] = 0;
        enter[i] = false;
    }
}

void add_edge(int u,int v,int w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
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
            if(dist[v] > dist[u] + w){
                dist[v] = dist[u] + w;
                if(!enter[v]){
                    if(++update[v]>n){
                        return true;
                    }
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
        int u,v,w;
        cin>>u>>v>>w;
        add_edge(v,u,w);
    }
    if(spfa(0)){
        cout<<"NO"<<"\n";
    }else{
        for(int i=1;i<=n;i++){
            cout<<dist[i]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
