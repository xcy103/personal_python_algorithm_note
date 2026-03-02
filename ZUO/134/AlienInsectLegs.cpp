#include<bits/stdc++.h>
using namespace std;

const int MAXN = 2005;
const int MAXS = 2005;

bitset<MAXS> mat[MAXN];

int n,m,s;
int need;

void gauss(int n){
    need = 0;
    for(int i=1;i<=n;i++){
        int povit = -1;
        for(int j=i;j<=n;j++){
            if(mat[j][i])
                povit = j;
                break;
        }
        if(povit == -1){
            return;
        }
        if(povit != i){
            swap(mat[i],mat[povit]);
        }
        need = max(need,povit);
        for(int j=1;j<=n;j++){
            if(j!=i && mat[j][i]){
                mat[j] ^= mat[i];
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m;

    s = max(m,n);

    for(int i=1;i<=m;i++){
        string line;
        cin>>line;
        for(int j=1;j<=n;j++){
            if(line[j-1]=='1'){
                mat[i].set(j);
            }
        }
        int x;
        cin>>x;
        if(x==1){
            mat[i].set(s+1);
        }
    }
    gauss(s);

    for(int i=1;i<=n;i++){
        if(!mat[i][i]){
            cout<<"Cannot Determine"<<"\n";
            return 0;
        }
    }
    cout<<need<<"\n";
    for(int i=1;i<=n;i++){
        if(mat[i][s+1]){
            cout<<"?y7M#"<<"\n";
        }else{
            cout<<"Earth"<<"\n";
        }
    }
    return 0;
}