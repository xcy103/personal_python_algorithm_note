// 格子全变成0的操作方案
// 有一个n*m的二维网格，给定每个网格的初始值，一定是0、1、2中的一个
// 如果某个网格获得了一些数值加成，也会用%3的方式变成0、1、2中的一个
// 比如有个网格一开始值是1，获得4的加成之后，值为(1+4)%3 = 2
// 有一个神奇的刷子，一旦在某个网格处刷一下，该网格会获得2的加成
// 并且该网格上、下、左、右的格子，都会获得1的加成
// 最终目标是所有网格都变成0，题目保证一定有解，但不保证唯一解
// 得到哪一种方案都可以，打印一共需要刷几下，并且把操作方案打印出来
// 1 <= n、m <= 30
// 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5755

#include <iostream>
using namespace std;

const int MOD = 3;
const int MAXS = 1001;

int mat[MAXS][MAXS],inv[MOD],n,m,s;
int dir[5] = {0,-1,0,1,0};

void inv_init(){
    inv[1] = 1;
    for(int i=2;i<MOD;i++){
        inv[i] = (MOD - (long long)inv[MOD%i]*(MOD/i)%MOD + MOD)%MOD;
    }
}

int gcd(int a,int b){
    return b==0?a:gcd(b,a%b);
}
void prepare(){
    for(int i=1;i<=s;i++){
        for(int j=1;j<=s+1;j++){
            mat[i][j] = 0;
        }
    }

    int cur,row,col;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cur = i*m+j+1;
            mat[cur][cur] = 2;
            for(int d=0;d<4;d++){
                row = i+dir[d];
                col = j+dir[d+1];
                if(row>=0&&row<n&&col>=0&&col<m){
                    mat[cur][row*m+col+1] = 1;
                }
            }
        }
    }
}

void swap_row(int i,int j){
    for(int k=1;k<=s+1;k++){
        swap(mat[i][k],mat[j][k]);
    }
}

void gauss(){
    for(int i=1;i<=s;i++){
        for(int j=1;j<=s;j++){
            if(j<i&&mat[j][j]) continue;

            if(mat[j][i]){
                swap_row(i,j);
                break;
            }
        }
        if(mat[i][i]==0) continue;

        for(int j=1;j<=s;j++){
            if(i!=j&&mat[j][i]){
                int g = gcd(mat[j][i],mat[i][i]);
                int a = mat[i][i]/g,b = mat[j][i]/g;

                if(j<i&&mat[j][j]){
                    mat[j][j] = (mat[j][j]*a)%MOD;
                }

                for(int k=i;k<=s+1;k++){
                    mat[j][k] = ((mat[j][k]*a - mat[i][k]*b)%MOD + MOD)%MOD;

                }
            }
        }
    }

    for(int i=1;i<=s;i++){
        if(mat[i][i]){
            mat[i][s+1] = (mat[i][s+1]*inv[mat[i][i]])%MOD;
            mat[i][i] = 1;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    inv_init();
    int t;
    cin>>t;
    while(t--){
        cin>>n>>m;
        s = n*m;
        prepare();

        for(int i=1;i<=s;i++){
            int x;
            cin>>x;
            mat[i][s+1] = (3-x)%MOD;
        }
        gauss();
        int ans = 0;
        for(int i=1;i<=s;i++){
            ans+=mat[i][s+1];
        }
        cout<<ans<<'\n';
        for(int i=1,id=1;i<=n;i++){
            for(int j=1;j<=m;j++,id++){
                while(mat[id][s+1]-->0){
                    cout<<i<<" "<<j<<'\n';
                }
            }
        }
    }
    return 0;
}