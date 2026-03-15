//这道题想到每个边减去一个二分值，判断有没有环之和大于0，来二分比较容易想到
//但是到底该怎么判断负环不好象，左的做法是，定一个超级源点，也可以写一个循环来判断
//开始dfs递归，来到一个点，标记为true，再看他的子节点，如果到子节点的边可以使得
//子节点的累计点权边的更小，就走，不然就不走，如果来到一个点发现，这个点已经在路径上
//或者从这个点出发，dfs返回true，就说明找到一个负环，check函数就要返回true
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

const int MAXN = 3001;
const int MAXM = 10001;
const double MAXE = 1e7;
const double sml = 1e-9;

int cnt,head[MAXN],nxt[MAXM],to[MAXM];
double weight[MAXM];

// dfs判断负环
double value[MAXN];
bool path[MAXN];

int n,m;

void prepare(){
    cnt = 1;
    for(int i=1;i<=n;i++){
        head[i] = 0;
    }
}

void addEdge(int u,int v,double w){
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}

// 所有边减去 x，判断是否存在负环
bool dfs(int u, double x){
    path[u] = true;
    for(int e = head[u];e;e = nxt[e]){
        int v = to[e];
        double w = weight[e] - x;
        //如果继续向下走，可以使得子节点累计边权变小，则继续往下走
        if(value[v] > value[u] + w){
            value[v] = value[u] + w;
            if(path[v] || dfs(v,x)){
                return true;
            }
        }
    }
    path[u] = false;
    return false;
}

bool check(double x){
    for(int i=1;i<=n;i++){
        value[i] = 0;
        path[i] = false;
    }
    // 等价于加一个超级源点 0
    for(int i=1;i<=n;i++){
        if(dfs(i,x)){
            return true;
        }
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    prepare();

    for(int i=1;i<=m;i++){
        int u,v;
        double w;
        cin >> u >> v >> w;
        addEdge(u,v,w);
    }

    double l = -MAXE,r = MAXE;
    while(l+sml<r){
        double mid = (l+r)/2;
        if(check(mid)){
            r = mid;
        }else{
            l = mid;
        }
    }
    printf("%.8f\n", l);
    return 0;
}