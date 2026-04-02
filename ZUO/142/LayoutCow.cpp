// 布局奶牛
// 编号1到编号n的奶牛从左往右站成一排，你可以决定任意相邻奶牛之间的距离
// 有m1条好友信息，有m2条情敌信息，好友间希望距离更近，情敌间希望距离更远
// 每条好友信息为 : u v w，表示希望u和v之间的距离 <= w，输入保证u < v
// 每条情敌信息为 : u v w，表示希望u和v之间的距离 >= w，输入保证u < v
// 你需要安排奶牛的布局，满足所有的好友信息和情敌信息
// 如果不存在合法方案，返回-1
// 如果存在合法方案，返回1号奶牛和n号奶牛之间的最大距离
// 如果存在合法方案，并且1号奶牛和n号奶牛之间的距离可以无穷远，返回-2
// 测试链接 : https://www.luogu.com.cn/problem/P4878

#include<bits/stdc++.h>
using namespace std;

const int MAXN = 1001;
const int MAXM = 20001;
const int MAXQ = 1000001;

int head[MAXN],nxt[MAXM],to[MAXM],weight[MAXM],cnt;

int dist[MAXN],update[MAXN];
bool enter[MAXN];
int q[MAXQ],h,t;

int n,m1,m2;

void prepare(){
    cnt = 1;
    memset(head,0,sizeof(head));
}

void add_edge(int u,int v,int w){ 
    nxt[cnt] = head[u];
    to[cnt] = v;
    weight[cnt] = w;
    head[u] = cnt++;
}   
int spfa(int s){
    h = t = 0;
    for(int i=0;i<=n;i++){
        dist[i] = INT_MAX;
        update[i] = 0;
        enter[i] = false;
    }
    dist[s] = 0;
    update[s] = 1;
    enter[s] = true;
    q[t++] = s;
    while(h<t){
        int u = q[h++];
        enter[u] = false;
        for(int e=head[u];e;e=nxt[e]){
            int v = to[e];
            int w = weight[e];
            if(dist[v]>dist[u]+w){
                dist[v] = dist[u] + w;
                if(++update[v]>n) return -1;
                if(!enter[v]){
                    q[t++] = v;
                    enter[v] = true;
                }
            }
        }
    }
    if(dist[n] == INT_MAX) return -2;
    return dist[n];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>m1>>m2;

    prepare();
    for(int i=1;i<=n;i++){
        add_edge(0,i,0);
    }

    for(int i=1;i<=m1;i++){
        int u,v,w;
        cin>>u>>v>>w;
        add_edge(u,v,w);
    }
    for(int i=1;i<=m2;i++){
        int u,v,w;
        cin>>u>>v>>w;
        add_edge(v,u,-w);
    }
    for(int i=1;i<n;i++){
        add_edge(i+1,i,0);
    }
    int ans = spfa(0);
    if(ans == -1){
        cout<<ans<<"\n";
    }else{
        ans = spfa(1);
        cout<<ans<<"\n";
    }
    return 0;

}