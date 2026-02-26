#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAXN = 200000 + 5;

ll arr[MAXN];
ll sum_tree[MAXN << 2];
ll lazy_tree[MAXN << 2];

void push_up(int i) {
    sum_tree[i] = sum_tree[i<<1] + sum_tree[i<<1|1];
}

void apply(int i, ll v, int len) {
    sum_tree[i] += v * len;
    lazy_tree[i] += v;
}

void push_down(int i, int ln, int rn) {
    if (lazy_tree[i]) {
        apply(i<<1, lazy_tree[i], ln);
        apply(i<<1|1, lazy_tree[i], rn);
        lazy_tree[i] = 0;
    }
}

void build(int l, int r, int i) {
    if (l == r) {
        sum_tree[i] = arr[l];
        return;
    }
    int mid = (l + r) >> 1;
    build(l, mid, i<<1);
    build(mid+1, r, i<<1|1);
    push_up(i);
}

void update(int L, int R, ll v, int l, int r, int i) {
    if (L <= l && r <= R) {
        apply(i, v, r - l + 1);
        return;
    }
    int mid = (l + r) >> 1;
    push_down(i, mid - l + 1, r - mid);

    if (L <= mid)
        update(L, R, v, l, mid, i<<1);
    if (R > mid)
        update(L, R, v, mid+1, r, i<<1|1);

    push_up(i);
}

ll query(int L, int R, int l, int r, int i) {
    if (L <= l && r <= R)
        return sum_tree[i];

    int mid = (l + r) >> 1;
    push_down(i, mid - l + 1, r - mid);

    ll ans = 0;
    if (L <= mid)
        ans += query(L, R, l, mid, i<<1);
    if (R > mid)
        ans += query(L, R, mid+1, r, i<<1|1);

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    for (int i = 1; i <= n; i++)
        cin >> arr[i];

    build(1, n, 1);

    while (q--) {
        int op;
        cin >> op;

        if (op == 1) {
            int l, r;
            ll v;
            cin >> l >> r >> v;
            update(l, r, v, 1, n, 1);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query(l, r, 1, n, 1) << '\n';
        }
    }

    return 0;
}