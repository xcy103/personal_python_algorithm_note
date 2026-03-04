//这道题是，有很多确定值的变量，如果两两确定值之间设置边
//如果已知变量很多，那么就n^3超时
// 题目4，倍杀测量者，另一种二分的写法
// 思路是不变的，二分的写法多种多样
// 代码中打注释的位置，就是更简单的二分逻辑，其他代码没有变化
// 测试链接 : https://www.luogu.com.cn/problem/P4926

#include<bits/stdc++.h>
using namespace std;

const int MAXN = 1002;
const int MAXM = 3001;
const double INF = 1e10;

int n,m1,m2,vow[MAXN][4],score[MAXN][2];
//链式前向星
int head[MAXN],nxt[MAXM],to[MAXM],cnt;
double weight[MAXM];
//spfa
double dist[MAXN];
int update[MAXN];

const int MAXQ = 1000001;
int q[MAXQ],h,t;
bool enter[MAXN];

void prepare(){
    cnt = 1;
    h = t = 0;
    for(int i=1;i<=n+1;i++){
        head[i] = 0;
        dist[i] = INF;
        enter[i] = false;
        update[i] = 0;
    }
}

void add_edge(int u,int v,double w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}

bool spfa(int s){
    dist[s] = 0;
    update[s] = 1;
    q[t++] = s;
    enter[s] = true;
    while(h<t){
        int u = q[h++];
        enter[u] = false;
        for(int e=head[u];e;e=nxt[e]){
            int v = to[e];
            double w = weight[e];
            if(dist[v] > dist[u] + w){
                dist[v] = dist[u] + w;
                if(!enter[v]){
                    if(++update[v] > n+1){
                        return true;
                    }
                    q[t++] = v;
                    enter[v] = true;
                }
            }
        }
    }
    return false;
}

bool check(double limit){
    prepare();
    for(int i=1;i<=n;i++){
        add_edge(0,i,0);
    }
    for(int i=1;i<=m1;i++){
        if(vow[i][0] == 1){
            if(-limit + vow[i][3]>=0){
                add_edge(vow[i][1],vow[i][2],-log(-limit+vow[i][3]));
            }
        }else{
            add_edge(vow[i][1],vow[i][2],log(limit+vow[i][3]));
        }
    }
    for(int i=1;i<=m2;i++){
        add_edge(n+1,score[i][0],log(score[i][1]));
        add_edge(score[i][0],n+1,-log(score[i][1]));
    }
    return spfa(0);
}

double compute(){
    double l = 0,r = INF,ans = 0,m;
    for(int i=1;i<=60;i++){
        m = (l+r)/2;
        if(check(m))l=m;
        else r=m;
    }
    return l;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m1>>m2;
    for(int i=1;i<=m1;i++){
        cin>>vow[i][0]>>vow[i][1]>>vow[i][2]>>vow[i][3];
    }
    for(int i=1;i<=m2;i++){
        cin>>score[i][0]>>score[i][1];
    }
    double ans = compute();
    if(ans==0) cout<<-1<<"\n";
    else cout<<ans<<"\n";

    return 0;

}


