#include<bits/stdc++.h>
using namespace std;

const int MAXN = 102;
const double sml = 1e-9;

int n,arr[MAXN][MAXN];
double mat[MAXN][MAXN];


void gauss(int n){
    for(int i=1;i<=n;i++){
        int max_row = i;
        for(int j=1;j<=n;j++){
            if(j<i && fabs(mat[j][j])>=sml) continue;
            if(fabs(mat[j][i])>fabs(mat[max_row][i])){
                max_row = j;
            }
        }
        for(int j=1;j<=n+1;j++) swap(mat[i][j],mat[max_row][j]);

        if(fabs(mat[i][i])>=sml){
            double pivot = mat[i][i];
            for(int j=i;j<=n+1;j++){
                mat[i][j] /= pivot; 
            }

            for(int j=1;j<=n;j++){
                if(j==i) continue;
                double val = mat[j][i];
                for(int k=i;k<=n+1;k++){
                    mat[j][k] -= val*mat[i][k];
                }
            }
        }
    }
}
int check(){ 
    gauss(n);
    int maxv = -1,maxt = 0,ans = 0;
    for(int i=1;i<=n;i++){
        if(fabs(mat[i][i])<sml) return 0;

        double val=mat[i][n+1];

        if(val<=0 || fabs(val-round(val))>sml) return 0;
        
        int v = (int)round(val);

        if(v>maxv){
            maxv = v;
            maxt = 1;
            ans = i;
        }else if(v==maxv){
            maxt++;
        }
    }
    if(maxt>1) return 0;
    return ans;
}
int main(){
    ios::sync_with_stdio(false);  
    cin.tie(0);

    cin>>n;
    for(int i=1;i<=n+1;i++){
        int m;
        cin>>m;
        for(int j=1;j<=m;j++){
            int cur;
            cin>>cur;
            arr[i][cur] = 1;
        }
        cin>>arr[i][n+1];
    }   
    int ans = 0,times = 0;
    for(int k=1;k<=n+1;k++){
        for(int j=1;j<=n+1;j++) swap(arr[k][j],arr[n+1][j]);

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n+1;j++){
                mat[i][j] = arr[i][j];
            }
        }
        
        for(int j=1;j<=n+1;j++) swap(arr[k][j],arr[n+1][j]);
        int cur = check();
        if(cur!=0){
            times++;
            ans = cur;
        }
        
    }
    if(times!=1) cout<<"illegal"<<endl;
    else cout<<ans<<endl;
    return 0;
}