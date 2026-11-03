class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
        res = []
        rem = sum
        for i in range(num):
            pos_left = num - i - 1
            lo = 1 if i == 0 else 0
            for d in range(9, lo - 1, -1):
                r = rem - d
                if 0 <= r <= 9 * pos_left:
                    res.append(str(d))
                    rem = r
                    break
            else:
                return ""
        return "".join(res)