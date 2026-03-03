#include <bits/stdc++.h>
using namespace std;

// 最大异或和
// 线性基模板
// n <= 50
// arr[i] <= 2^50

const int MAXN = 51;
const int BIT = 50;

long long arr[MAXN];
long long basis[BIT + 1];
int n;

// 向线性基中插入一个数
// 若成功插入返回 true，否则 false
bool insert_basis(long long num) {
    for (int i = BIT; i >= 0; i--) {
        if ((num >> i) & 1LL) {   // 判断第 i 位是否为 1
            if (!basis[i]) {
                basis[i] = num;
                return true;
            }
            num ^= basis[i];
        }
    }
    return false;
}

// 计算最大异或和
long long compute() {
    for (int i = 1; i <= n; i++) {
        insert_basis(arr[i]);
    }
    long long ans = 0;
    for (int i = BIT; i >= 0; i--) {
        ans = max(ans, ans ^ basis[i]);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    cout << compute() << "\n";
    return 0;
}