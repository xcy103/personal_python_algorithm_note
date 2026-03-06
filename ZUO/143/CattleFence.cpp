/*
Author: yangka
Date: 2026-03-04
*/
// 牛场围栏
// 给定一个长度为n的数组arr, arr[i]代表第i种木棍的长度，每种木棍有无穷多个
// 给定一个正数m，表示你可以把任何一根木棍消去最多m的长度，同一种木棍可以消去不同的长度
// 你可以随意拼接木棍形成一个长度，返回不能拼出来的长度中，最大值是多少
// 如果你可以拼出所有的长度，返回-1
// 如果不能拼出来的长度有无穷多，返回-1
// 1 <= n <= 100
// 1 <= arr[i] <= 3000
// 1 <= m <= 3000
// 测试链接 : https://www.luogu.com.cn/problem/P2662

#include <bits/stdc++.h>
using namespace std;

using ll  = long long;
using pli = pair<ll,int>;
using minpq = priority_queue<pli, vector<pli>, greater<pli>>;

const int MAXN = 101;
const int MAXV = 3001;
const int MAXM = 30001;
const int inf = INT_MAX;

int n,m,x;
int arr[MAXN];
bool st[MAXV];
// 链式前向星
int head[MAXV], nxt[MAXM], to[MAXM], cnt;
int weight[MAXM];
int dist[MAXV];
bool vis[MAXV];
minpq pq;
void add_edge(int u,int v,int w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}

void prepare(){
    cnt = 1;
    while(!pq.empty()) pq.pop();
    memset(head, 0, sizeof(head));
    memset(st, false, sizeof(st));
    for(int i=0;i<x;i++){
        dist[i] = inf;
        vis[i] = false;
    }
}
void dijkstra(){
    pq.push({0,0});
    dist[0] = 0;
    while(!pq.empty()){
        auto [d,u] = pq.top();
        pq.pop();
        if(vis[u]) continue;
        vis[u] = true;
        for(int e=head[u];e;e=nxt[e]){
            int v = to[e];
            if(!vis[v] && dist[v] > dist[u] + weight[e]){
                dist[v] = dist[u] + weight[e];
                pq.push({dist[v],v});
            }
        }
    }
}

int compute(){
    int ans = 0;
    if(x==1){
        ans = -1;
    }else{
        for(int i=1;i<=n;i++){
            for(int j=max(1,arr[i] - m);j<=arr[i];j++){
                if(!st[j]){
                    st[j] = true;
                    for(int k=0;k<x;k++){
                        add_edge(k,(k+j)%x,j);
                    }

                }
            }
        }
        dijkstra();

        for(int i=1;i<x;i++){
            if(dist[i] == inf){
                ans = -1;
                break;
            }
            ans = max(ans,dist[i] - x);
        }
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m;
    x = inf;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
        x = min(x,max(1,arr[i] - m));
    }
    prepare();
    cout<<compute()<<"\n";
    

    return 0;
}