#其实就是学了一些技巧，从左那里学到得用fix，标记之前是否选过数字
#第二个技巧看别的题目
#左还教了打表法，但是感觉不是很必要
class Solution:

    # 方法1：递归
    def atMostNGivenDigitSet(self, strs, num):
        tmp = num // 10
        length = 1
        offset = 1

        while tmp > 0:
            tmp //= 10
            length += 1
            offset *= 10

        digits = [int(x) for x in strs]

        return self.f1(digits, num, offset, length, 0, 0)

    def f1(self, digits, num, offset, length, free, fix):
        if length == 0:
            return 1 if fix == 1 else 0

        ans = 0
        cur = (num // offset) % 10

        if fix == 0:
            ans += self.f1(digits, num, offset // 10, length - 1, 1, 0)

        if free == 0:
            for d in digits:
                if d < cur:
                    ans += self.f1(digits, num, offset // 10, length - 1, 1, 1)
                elif d == cur:
                    ans += self.f1(digits, num, offset // 10, length - 1, 0, 1)
                else:
                    break
        else:
            ans += len(digits) * self.f1(digits, num, offset // 10, length - 1, 1, 1)

        return ans


    # 方法2：优化版
    def atMostNGivenDigitSet2(self, strs, num):
        digits = [int(x) for x in strs]
        m = len(digits)

        length = 1
        offset = 1
        tmp = num // 10

        while tmp > 0:
            tmp //= 10
            length += 1
            offset *= 10

        cnt = [0] * length
        cnt[0] = 1

        ans = 0
        i = m
        for k in range(1, length):
            cnt[k] = i
            ans += i
            i *= m

        return ans + self.f2(digits, cnt, num, offset, length)

    def f2(self, digits, cnt, num, offset, length):
        if length == 0:
            return 1

        cur = (num // offset) % 10
        ans = 0

        for d in digits:
            if d < cur:
                ans += cnt[length - 1]
            elif d == cur:
                ans += self.f2(digits, cnt, num, offset // 10, length - 1)
            else:
                break

        return ans