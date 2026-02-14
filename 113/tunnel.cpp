#include <iostream>
#include <vector>
#include <stack>
#include <set>

using namespace std;

void solve() {
    int n, m;
    // 处理多组输入，直到文件末尾
    while (cin >> n >> m) {
        set<int> destroyed;
        stack<int> history;
        
        // 为了方便处理边界，我们在 0 和 n+1 位置各增加一个“虚拟摧毁房屋”
        destroyed.insert(0);
        destroyed.insert(n + 1);
        
        char op;
        int x;
        for (int i = 0; i < m; ++i) {
            cin >> op;
            if (op == 'D') {
                cin >> x;
                destroyed.insert(x);
                history.push(x);
            } else if (op == 'R') {
                if (!history.empty()) {
                    destroyed.erase(history.top());
                    history.pop();
                }
            } else if (op == 'Q') {
                cin >> x;
                // 如果当前房子已被摧毁，能到达的数量为 0
                if (destroyed.count(x)) {
                    cout << 0 << "\n";
                } else {
                    // 使用 lower_bound 找到第一个大于或等于 x 的元素 (右边界)
                    auto it_right = destroyed.lower_bound(x);
                    // 右边界的前一个元素即为左边界
                    auto it_left = prev(it_right);
                    
                    // 结果 = 右边界坐标 - 左边界坐标 - 1
                    cout << (*it_right - *it_left - 1) << "\n";
                }
            }
        }
    }
}

int main() {
    // 提高 I/O 效率
    ios::sync_with_stdio 