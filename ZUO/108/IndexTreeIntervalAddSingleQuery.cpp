#include<bits/stdc++.h>
using namespace std;

const int MAXN = 500002;
#define ll long long

int n,m;
ll tree[MAXN];

void add(int i, int v){
    while(i<=n){
        tree[i]+=v;
        i+=(i&-i);
    }
}

ll sum(int i){
    ll ans = 0;
    while(i>0){
        ans+=tree[i];
        i&=(i-1);
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m;

    for(int i=1;i<=n;i++){
        ll v;
        cin>>v;
        add(i,v);
        add(i+1,-v);
    }

    for(int i=0;i<m;i++){
        int op;
        cin>>op;
        if(op==1){
            int l,r;
            ll v;
            cin>>l>>r>>v;
            add(l,v);
            add(r+1,-v);
        }
        else{
            int idx;
            cin>>idx;
            cout<<sum(idx)<<"\n";
        }
    }
    return 0;
}