//两次转圈写法。优化时间复杂度O(n*x)
/*
Author: yangka
Date: 2026-03-05 13:08:07
*/

#include <bits/stdc++.h>
using namespace std;

using ll  = long long;
using pli = pair<ll,int>;
using minpq = priority_queue<pli, vector<pli>, greater<pli>>;

const int MAXN = 500001;
const int MAXM = 2000005;
const ll inf = LLONG_MAX;
int v[MAXN],n,x;
ll dist[MAXN],l,r;
// 链式前向星
int head[MAXN], nxt[MAXM], to[MAXM], cnt;
double weight[MAXM];

void add_edge(int u,int v,double w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}
int gcd(int a,int b){
    return b == 0 ? a : gcd(b,a%b);
}
ll compute(){
    sort(v+1,v+n+1);
    int size = 0;
    for(int i=1;i<=n;i++){
        if(v[i]!=0){
            v[++size] = v[i];
        }
    }
    if(size==0)return 0;
    x = v[1];
    for(int i=0;i<x;i++){
        dist[i] = inf;
    }
    dist[0] = 0;
    for(int i=2;i<=size;i++){
        int d = gcd(x,v[i]);
        for(int j=0;j<d;j++){
            int cur = j;
            int c = 0;
            while(c<2){
                int next = (cur+v[i])%x;
                if(dist[cur]!=inf){
                    dist[next] = min(dist[next],dist[cur]+v[i]);
                }
                cur = next;
                if(cur==j)c++;
            }
        }
    }
    ll ans = 0;
    for(int i=0;i<x;i++){
        if(r>=dist[i]){
            ans+=(r-dist[i])/x + 1;
        }
        if(l>=dist[i]){
            ans-=(l-dist[i])/x + 1;
        }
    }
    return ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>l>>r;
    l--;
    for(int i=1;i<=n;i++){
        cin>>v[i];
    }
    cout<<compute()<<"\n";

    return 0;
}