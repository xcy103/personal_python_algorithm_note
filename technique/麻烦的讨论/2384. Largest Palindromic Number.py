class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = [0] * 58
        for c in num:
            cnt[ord(c)] += 1

        ans = [''] * len(num)
        left_size = 0
        mid = ''

        # 先处理 1~9（避免前导0）
        for i in range(ord('9'), ord('0'), -1):
            if cnt[i] % 2 == 1 and mid == '':
                mid = chr(i)
            for _ in range(cnt[i] // 2):
                ans[left_size] = chr(i)
                left_size += 1

        # 特判：左边为空
        if left_size == 0:
            if mid == '':
                return "0"
            else:
                return mid

        # 加 0
        for _ in range(cnt[ord('0')] // 2):
            ans[left_size] = '0'
            left_size += 1

        length = left_size

        # 中间
        if mid == '' and cnt[ord('0')] % 2 == 1:
            mid = '0'
        if mid != '':
            ans[length] = mid
            length += 1

        # 镜像
        for i in range(left_size - 1, -1, -1):
            ans[length] = ans[i]
            length += 1

        return ''.join(ans[:length])