class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        num_seen = False      # 是否出现过数字
        dot_seen = False      # 是否出现过 .
        e_seen = False        # 是否出现过 e/E
        num_after_e = True    # e 后面是否有数字

        for i, c in enumerate(s):
            if c.isdigit():
                num_seen = True
                num_after_e = True

            elif c in ['+', '-']:
                # 只能在开头 或 e 后面
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False

            elif c == '.':
                # 不能有多个 . 或 在 e 后面
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            elif c in ['e', 'E']:
                # 不能有多个 e，且前面必须有数字
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False

            else:
                return False

        return num_seen and num_after_e