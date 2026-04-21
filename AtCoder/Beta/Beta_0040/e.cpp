#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Employee {
    int x, v;
    bool operator<(const Employee& other) const {
        return x < other.x;
    }
};

struct Query {
    int l, r, id, blk;
    bool operator<(const Query& other) const {
        if (blk != other.blk) return blk < other.blk;
        // 奇偶块优化，提升莫队算法右指针移动的效率
        return (blk & 1) ? r < other.r : r > other.r; 
    }
};

int main() {
    // 开启 Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<Employee> emp(N);
    vector<int> vals(N);
    for (int i = 0; i < N; ++i) {
        cin >> emp[i].x >> emp[i].v;
        vals[i] = emp[i].v;
    }

    // 1. 按坐标排序
    sort(emp.begin(), emp.end());

    // 2. 离散化分数 (Coordinate Compression)
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    for (int i = 0; i < N; ++i) {
        // 将原分数映射到 0 ~ (不同分数的种类数 - 1)
        emp[i].v = lower_bound(vals.begin(), vals.end(), emp[i].v) - vals.begin();
    }

    // 提取排序后的坐标，方便二分查找
    vector<int> xs(N);
    for (int i = 0; i < N; ++i) {
        xs[i] = emp[i].x;
    }

    int block_size = max(1, (int)(N / sqrt(Q)));
    vector<Query> queries;
    vector<long long> ans(Q, 0);

    // 3. 读入并映射查询
    for (int i = 0; i < Q; ++i) {
        int L, R;
        cin >> L >> R;
        
        // 二分查找坐标区间对应的数组下标
        int l_idx = lower_bound(xs.begin(), xs.end(), L) - xs.begin();
        int r_idx = upper_bound(xs.begin(), xs.end(), R) - xs.begin() - 1;

        if (l_idx <= r_idx) {
            queries.push_back({l_idx, r_idx, i, l_idx / block_size});
        } else {
            ans[i] = 0; // 区间内没有员工
        }
    }

    // 4. 跑莫队算法
    sort(queries.begin(), queries.end());

    vector<int> cnt(vals.size(), 0);
    long long current_sum_sq = 0;
    int cur_l = 0, cur_r = -1;

    auto add = [&](int idx) {
        int v = emp[idx].v;
        long long c = cnt[v];
        current_sum_sq += 2 * c + 1; // (c+1)^2 - c^2 = 2c + 1
        cnt[v]++;
    };

    auto remove = [&](int idx) {
        int v = emp[idx].v;
        long long c = cnt[v];
        current_sum_sq -= 2 * c - 1; // c^2 - (c-1)^2 = 2c - 1
        cnt[v]--;
    };

    for (const auto& q : queries) {
        while (cur_l > q.l) { cur_l--; add(cur_l); }
        while (cur_r < q.r) { cur_r++; add(cur_r); }
        while (cur_l < q.l) { remove(cur_l); cur_l++; }
        while (cur_r > q.r) { remove(cur_r); cur_r--; }

        long long c = q.r - q.l + 1;
        // 使用我们推导的核心公式：(2c + c^2 - sum_sq) / 2
        ans[q.id] = (2 * c + c * c - current_sum_sq) / 2;
    }

    // 5. 输出结果
    for (int i = 0; i < Q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}