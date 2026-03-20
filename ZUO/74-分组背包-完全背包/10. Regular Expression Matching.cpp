// 正则表达式匹配
// 给你字符串s、字符串p
// s中一定不含有'.'、'*'字符，p中可能含有'.'、'*'字符
// '.' 表示可以变成任意字符，数量1个
// '*' 表示可以让 '*' 前面那个字符数量任意(甚至可以是0个)
// p中即便有'*'，一定不会出现以'*'开头的情况，也一定不会出现多个'*'相邻的情况(无意义)
// 请实现一个支持 '.' 和 '*' 的正则表达式匹配
// 返回p的整个字符串能不能匹配出s的整个字符串
// 测试链接 : https://leetcode.cn/problems/regular-expression-matching/


#include <bits/stdc++.h>
using namespace std;

class RegularExpressionMatching {
public:

    // =========================
    // 1. 纯递归
    // =========================
    static bool isMatch1(string str, string pat) {
        return f1(str, pat, 0, 0);
    }

    // s[i...] 是否能匹配 p[j...]
    static bool f1(const string& s, const string& p, int i, int j) {
        if (i == s.size()) {
            if (j == p.size()) {
                return true;
            } else {
                return j + 1 < p.size() && p[j + 1] == '*' && f1(s, p, i, j + 2);
            }
        } else if (j == p.size()) {
            return false;
        } else {
            if (j + 1 == p.size() || p[j + 1] != '*') {
                return (s[i] == p[j] || p[j] == '.') && f1(s, p, i + 1, j + 1);
            } else {
                // 不用 *
                bool p1 = f1(s, p, i, j + 2);
                // 用 *
                bool p2 = (s[i] == p[j] || p[j] == '.') && f1(s, p, i + 1, j);
                return p1 || p2;
            }
        }
    }

    // =========================
    // 2. 记忆化搜索
    // =========================
    static bool isMatch2(string str, string pat) {
        int n = str.size();
        int m = pat.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        return f2(str, pat, 0, 0, dp);
    }

    static bool f2(const string& s, const string& p, int i, int j, vector<vector<int>>& dp) {
        if (dp[i][j] != 0) {
            return dp[i][j] == 1;
        }

        bool ans;
        if (i == s.size()) {
            if (j == p.size()) {
                ans = true;
            } else {
                ans = j + 1 < p.size() && p[j + 1] == '*' && f2(s, p, i, j + 2, dp);
            }
        } else if (j == p.size()) {
            ans = false;
        } else {
            if (j + 1 == p.size() || p[j + 1] != '*') {
                ans = (s[i] == p[j] || p[j] == '.') && f2(s, p, i + 1, j + 1, dp);
            } else {
                ans = f2(s, p, i, j + 2, dp) ||
                      ((s[i] == p[j] || p[j] == '.') && f2(s, p, i + 1, j, dp));
            }
        }

        dp[i][j] = ans ? 1 : 2;
        return ans;
    }

    // =========================
    // 3. 严格DP（推荐）
    // =========================
    static bool isMatch3(string str, string pat) {
        int n = str.size();
        int m = pat.size();

        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        dp[n][m] = true;

        // 初始化 s为空 的情况
        for (int j = m - 1; j >= 0; j--) {
            if (j + 1 < m && pat[j + 1] == '*') {
                dp[n][j] = dp[n][j + 2];
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (j + 1 == m || pat[j + 1] != '*') {
                    dp[i][j] = (str[i] == pat[j] || pat[j] == '.') && dp[i + 1][j + 1];
                } else {
                    dp[i][j] = dp[i][j + 2] ||
                               ((str[i] == pat[j] || pat[j] == '.') && dp[i + 1][j]);
                }
            }
        }

        return dp[0][0];
    }
};