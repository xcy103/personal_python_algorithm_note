/*
Author: yangka
Date: 2026-03-05 15:10:26
*/

#include <bits/stdc++.h>
using namespace std;

using ll  = long long;
using pli = pair<ll,int>;
using minpq = priority_queue<pli, vector<pli>, greater<pli>>;

const int MAXN = 100001;
const int MAXM = 2000005;
const ll inf = LLONG_MIN;

int v[MAXN],c[MAXN];
ll dp[MAXN];
int n,m,x,y;

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
    return b==0?a:gcd(b,a%b);
}
void compute(){
    for(int i=0;i<x;i++){
        dp[i] = inf;
    }
    dp[0] = 0;
    for(int i=1;i<=n;i++){
        if(v[i]!=x){
            int d = gcd(x,v[i]);
            for(int j=0;j<d;j++){
                int cur = j;
                int cir = 0;
                while(cir<2){
                    int next = (cur+v[i])%x;
                    if(dp[cur]!=inf){
                        dp[next] = max(
                            dp[next],
                            dp[cur] - (ll)((cur + v[i]) / x) * y + c[i]
                        );
                    }
                    cur = next;
                    if(cur==j) cir++;
                }
            }
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m;

    double best = 0,ratio;

    for(int i=1;i<=n;i++){
        cin>>v[i]>>c[i];
        ratio = (double)c[i] / v[i];
        if (ratio > best) {
            best = ratio;
            x = v[i];
            y = c[i];
        }
    }
    compute();
    ll jobv;
    int mod;
    while(m--){
        cin>>jobv;
        mod = jobv%x;
        if(dp[mod]==inf){
            cout<<-1<<"\n";
        }else{
            cout<<(jobv/x)*y+dp[mod]<<"\n";
        }
    }

    return 0;
}