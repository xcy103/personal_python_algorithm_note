/*
Author: yangka
Date: 2026-03-13 18:01:46
*/

#include <bits/stdc++.h>
using namespace std;
using ll  = long long;
const int MAXN = 1001;
ll basis[64];
int n;
struct stone{
    ll number;
    ll values;
    bool operator<(const stone& rhs) const{
        return values>rhs.values;
    }
};

bool insert_basis(ll num){
    for(int i=63;i>=0;i--){
        if((num>>i)&1LL){
            if(!basis[i]){
                basis[i]=num;
                return true;
            }
            num^=basis[i];
        }
    }
    return false;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n;
    stone arr[MAXN];
    for(int i=0;i<n;i++){
        cin>>arr[i].number>>arr[i].values;
    }
    sort(arr,arr+n);
    ll ans = 0;
    for(int i=0;i<n;i++){
        if(insert_basis(arr[i].number)){
            ans+=arr[i].values;
        }
    }

    cout<<ans<<endl;
    return 0;
}