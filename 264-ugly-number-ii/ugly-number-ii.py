class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            next_ugly = min(
                dp[i2] * 2,
                dp[i3] * 3,
                dp[i5] * 5
            )

            dp[i] = next_ugly

            if next_ugly == dp[i2] * 2:
                i2 += 1
            if next_ugly == dp[i3] * 3:
                i3 += 1
            if next_ugly == dp[i5] * 5:
                i5 += 1

        return dp[-1]