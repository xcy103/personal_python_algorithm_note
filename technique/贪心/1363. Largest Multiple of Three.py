class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()
        total = sum(digits)

        mod1 = []  # %3 == 1
        mod2 = []  # %3 == 2

        for x in digits:
            if x % 3 == 1:
                mod1.append(x)
            elif x % 3 == 2:
                mod2.append(x)

        def remove(lst, k):
            if len(lst) < k:
                return False
            for _ in range(k):
                digits.remove(lst.pop(0))
            return True

        if total % 3 == 1:
            if not remove(mod1, 1):
                if not remove(mod2, 2):
                    return ""
        elif total % 3 == 2:
            if not remove(mod2, 1):
                if not remove(mod1, 2):
                    return ""

        if not digits:
            return ""

        digits.sort(reverse=True)

        # 去掉前导0
        if digits[0] == 0:
            return "0"

        return ''.join(map(str, digits))