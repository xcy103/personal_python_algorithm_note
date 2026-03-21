// 旅游，C++版
// 一共有n个城市，给定n-1条边，城市连成一棵树，每个城市给定初始的宝石价格
// 一共有m条操作，操作类型如下
// 操作 x y v : 城市x到城市y的最短路途中，你可以选择一城买入宝石
//              继续行进的过程中，再选一城卖出宝石，以此获得利润
//              打印你能获得的最大利润，如果为负数，打印0
//              当你结束旅途后，沿途所有城市的宝石价格增加v
// 1 <= n、m <= 5 * 10^4
// 0 <= 任何时候的宝石价格 <= 10^9
// 测试链接 : https://www.luogu.com.cn/problem/P3976
/*
Author: yangka
Date: 2026-03-20 17:43:26
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 50001;
const int INF  = 1000000001;

using ll  = long long;
int n,m, arr[MAXN];
//建图逻辑
int head[MAXN],nxt[MAXN<<1],to[MAXN<<1],cntg;
//树剖逻辑
int fa[MAXN],dep[MAXN],siz[MAXN],son[MAXN],top[MAXN],dfn[MAXN],seg[MAXN],cntd;
//线段树逻辑
int maxv[MAXN<<2],minv[MAXN<<2],lp[MAXN<<2],rp[MAXN<<2],addTag[MAXN<<2];

void addEdge(int u, int v) {
   nxt[++cntg] = head[u];
   to[cntg] = v;
   head[u] = cntg;
}

void dfs1(int u, int f) {
   fa[u] = f;
   dep[u] = dep[f] + 1;
   siz[u] = 1;
   for (int e = head[u]; e > 0; e = nxt[e]) {
       int v = to[e];
       if (v != f) {
           dfs1(v, u);
       }
   }
   for (int e = head[u]; e > 0; e = nxt[e]) {
       int v = to[e];
       if (v != f) {
           siz[u] += siz[v];
           if (son[u] == 0 || siz[son[u]] < siz[v]) {
               son[u] = v;
           }
       }
   }
}

void dfs2(int u, int t) {
   top[u] = t;
   dfn[u] = ++cntd;
   seg[cntd] = u;
   if (son[u] == 0) {
       return;
   }
   dfs2(son[u], t);
   for (int e = head[u]; e > 0; e = nxt[e]) {
       int v = to[e];
       if (v != fa[u] && v != son[u]) {
           dfs2(v, v);
       }
   }
}

void up(int i){
    int l = i<<1;
    int r = i<<1|1;
    maxv[i] = max(maxv[l],maxv[r]);
    minv[i] = min(minv[l],minv[r]);
    lp[i] = max({lp[l],lp[r],maxv[r]-minv[l]});
    rp[i] = max({rp[l],rp[r],maxv[l]-minv[r]});
}
void lazy(int i,int v){
    addTag[i]+=v;
    minv[i]+=v;
    maxv[i]+=v;
}
void down(int i) {
   if (addTag[i] != 0) {
       lazy(i << 1, addTag[i]);
       lazy(i << 1 | 1, addTag[i]);
       addTag[i] = 0;
   }
}
void build(int l, int r, int i) {
   if (l == r) {
       maxv[i] = minv[i] = arr[seg[l]];
   } else {
       int mid = (l + r) >> 1;
       build(l, mid, i << 1);
       build(mid + 1, r, i << 1 | 1);
       up(i);
   }
}
void add(int jobl,int jobr,int jobv,int l,int r,int i){
    if(jobl<=l && jobr>=r) lazy(i,jobv);
    else{
        down(i);
        int mid = (l + r) >> 1;
        if (jobl <= mid) {
            add(jobl, jobr, jobv, l, mid, i << 1);
        }
        if (jobr > mid) {
            add(jobl, jobr, jobv, mid + 1, r, i << 1 | 1);
        }
        up(i);
    }
}
void merge(int ans[],int rmax,int rmin,int rlp,int rrp){
    int lmax = ans[0];
    int lmin = ans[1];
    int llp  = ans[2];
    int lrp  = ans[3];
    ans[0] = max(lmax, rmax);
    ans[1] = min(lmin, rmin);
    ans[2] = max({llp, rlp, rmax - lmin});
    ans[3] = max({lrp, rrp, lmax - rmin});
}
void query(int ans[],int jobl, int jobr, int l, int r, int i){
    if(jobl<=l && jobr>=r){
        merge(ans, maxv[i], minv[i], lp[i], rp[i]);
    }else {
        down(i);
        int mid = (l + r) >> 1;
        if (jobl <= mid) {
            query(ans, jobl, jobr, l, mid, i << 1);
        }
        if (jobr > mid) {
            query(ans, jobl, jobr, mid + 1, r, i << 1 | 1);
        }
    }
}
void query(int ans[], int jobl, int jobr) {
   ans[0] = -INF;
   ans[1] =  INF;
   ans[2] =  0;
   ans[3] =  0;
   query(ans, jobl, jobr, 1, n, 1);
}
void clone(int *a, int *b) {
   a[0] = b[0];
   a[1] = b[1];
   a[2] = b[2];
   a[3] = b[3];
}
int compute(int x,int y,int v){
    int tmpx = x;
    int tmpy = y;
    int xpath[4] = {-INF, INF, 0, 0};
    int ypath[4] = {-INF, INF, 0, 0};
    int cur[4];
    //之前好奇为甚x,y查出的信息都和并在cur里面，因为x,y都是靠右的
    //cur始终作为最左的区间
    while(top[x]!=top[y]){
        if(dep[top[x]]<=dep[top[y]]){
            query(cur, dfn[top[y]], dfn[y]);
            merge(cur, ypath[0], ypath[1], ypath[2], ypath[3]);
            clone(ypath,cur);
            y = fa[top[y]];
        }else{
            query(cur, dfn[top[x]], dfn[x]);
            merge(cur, xpath[0], xpath[1], xpath[2], xpath[3]);
            clone(xpath,cur);
            x = fa[top[x]];
        }
    }
    //这个容易迷惑，其实就是一个设定，如果x比y浅
    //相当于是y跳到x，这是一个更右的区间，然后再和ypath比较

    if (dep[x] <= dep[y]) {
        query(cur, dfn[x], dfn[y]);
        merge(cur, ypath[0], ypath[1], ypath[2], ypath[3]);
        clone(ypath, cur);
    } else {
        query(cur, dfn[y], dfn[x]);
        merge(cur, xpath[0], xpath[1], xpath[2], xpath[3]);
        clone(xpath, cur);
    }
    //这里是因为要从x走到y，先比较x走到lca，再比较lca走到y
    //最后比较x的最小值和y的最大值
    int ans = max({xpath[3], ypath[2], ypath[0] - xpath[1]});
    x = tmpx;
    y = tmpy;
    while (top[x] != top[y]) {
        if (dep[top[x]] <= dep[top[y]]) {
            add(dfn[top[y]], dfn[y], v, 1, n, 1);
            y = fa[top[y]];
        } else {
            add(dfn[top[x]], dfn[x], v, 1, n, 1);
            x = fa[top[x]];
        }
    }
    add(min(dfn[x], dfn[y]), max(dfn[x], dfn[y]), v, 1, n, 1);
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        addEdge(u, v);
        addEdge(v, u);
    }
    dfs1(1, 0);
    dfs2(1, 1);
    build(1, n, 1);
    cin >> m;
    for (int i = 1; i <= m; i++) {
        int x, y, v;
        cin >> x >> y >> v;
        cout << compute(x, y, v) << "\n";
    }
    return 0;
}