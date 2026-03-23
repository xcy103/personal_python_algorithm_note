#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 20;

ll tri[MAXN][MAXN];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin>>n;

    for(int i=0;i<n;i++){
        tri[i][0] = tri[i][i] = 1;
    }

    for(int i=1;i<n;i++){
        for(int j=1;j<i;j++){
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j];
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            cout<<tri[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
