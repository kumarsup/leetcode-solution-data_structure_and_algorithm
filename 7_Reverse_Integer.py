class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        val = abs(x)
        sign = x // val

        res = 0

        while val > 0:
            remd = val % 10
            res = res * 10 + remd
            val = val // 10
        res = sign * res

        if -2 ** 31 <= res <= (2 ** 31) - 1:
            return res
        return 0