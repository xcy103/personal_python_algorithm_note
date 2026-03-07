#include<bits/stdc++.h>
using namespace std;

const int MOD = 1e6;
const int MAXN = 1001;
int f[MAXN];

void build(){
    f[0] = f[1] = 1;
    for(int i=2; i<MAXN; i++){
        for(int j=0;j<i;j++){
            f[i] = (f[i] + 1LL*f[j]*f[i-j-1])%MOD;
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    build();
    int n;
    while(cin >> n && n != 0){
        cout << f[n] << "\n";
    }
}