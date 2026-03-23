#include<bits/stdc++.h>
using namespace std;

using ll = long long;

const int MOD = 1e9 + 7;

ll power(ll x,ll p){
    ll ans = 1;
    while(p){
        if(p&1){
            ans = (ans * x) % MOD;
        }
        x = (x * x) % MOD;
        p >>= 1;

    }
    return ans;
}
int comb(int n,int k){
    ll fac = 1;
    int inv1 = 1;
    int inv2 = 1;

    for(int i=1;i<=n;i++){
        fac = (fac * i) % MOD;
        if(i==k){
            inv1 = power(fac,MOD-2);
        }
        if(i==n-k){
            inv2 = power(fac,MOD-2);
        }

    }
    return (int)(((fac*inv1)%MOD)*inv2%MOD);
}
int countOfPairs(vector<int>& arr){
    int n = arr.size();
    int k = arr[0] - 1;
    for(int i=1;i<n&&k>0;i++){
        if(arr[i-1]>arr[i]){
            k-=arr[i-1] - arr[i];
        }
    }
    if(k<=0) return 0;
    return comb(k+n-1,n);
}