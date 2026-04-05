#你需要特判m=1的情况
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        def check(m: int) -> bool:
            cnt = 0
            if m == 1:
                # 改成 0101...
                # 如果 s[i] 和 i 的奇偶性不同，cnt 加一
                cnt = sum((ord(b) ^ i) & 1 for i, b in enumerate(s))
                # n-cnt 表示改成 1010...
                cnt = min(cnt, n - cnt)
            else:
                k = 0
                for i, b in enumerate(s):
                    k += 1
                    # 到达连续相同子串的末尾
                    if i == n - 1 or b != s[i + 1]:
                        cnt += k // (m + 1)
                        k = 0
            return cnt <= numOps
        return bisect_left(range(n), True, 1, key=check)

