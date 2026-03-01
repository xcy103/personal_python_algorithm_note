#include<bits/stdc++.h>
using namespace std;
#define ll long long

const int MAXN = 100001;

int n,m;

ll info1[MAXN];
ll info2[MAXN];

void add(ll tree[],int i, ll v){
    while(i<=n){
        tree[i]+=v;
        i+=(i&-i);
    }
}

ll sum(ll tree[],int i){
    ll ans = 0;
    while(i>0){
        ans+=tree[i];
        i-=(i&-i);
    }
    return ans;
}

void range_add(int l, int r, ll v){
    add(info1,l,v);
    add(info1,r+1,-v);

    add(info2,l,(ll)(l-1)*v);
    add(info2,r+1,-(ll)(r)*v);

}
ll prefix_sum(int i){
    return sum(info1,i) * i - sum(info2,i);
}

ll range_sum(int l,int r){
    return prefix_sum(r) - prefix_sum(l-1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m;

    for(int i=1;i<=n;i++){
        ll cur;
        cin>>cur;
        range_add(i, i, cur);
    }
    for(int i=0;i<m;i++){
        int op;
        cin>>op;

        if(op==1){
            int l,r;
            ll v;
            cin>>l>>r>>v;
            range_add(l,r,v);
        }
        else{
            int l,r;
            cin>>l>>r;
            cout<<range_sum(l,r)<<'\n';
        }
    }
    return 0;
}