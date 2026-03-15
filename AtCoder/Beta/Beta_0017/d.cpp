#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 18;
int arr[MAXN+1];
ll cost[MAXN+1][MAXN+1];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n,m,k;
    cin>>n>>m>>k;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    for(int i=1;i<=m;i++){
        int u,v,b;
        cin>>u>>v>>b;
        cost[u][v] = b;
    }
    ll ans = LLONG_MIN;
    for(int mask=1;mask<(1<<(n+1));mask++){
        int c = 0;
        ll values = 0;
        vector<int> idx;
        for(int i=1;i<=n;i++){
            if(mask>>i&1){
                values+=arr[i];
                idx.push_back(i);
                c++;
            }
        }
        if(c!=k) continue;
        for(int x=0;x<k-1;x++){
            for(int y=x+1;y<k;y++){
                values-=cost[idx[x]][idx[y]];
            }
        }
        ans = max(ans,values);
    }
    cout<<ans<<"\n";
    return 0;
}
