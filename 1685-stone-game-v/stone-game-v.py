class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * (n + 1) for _ in range(n)]
        left_best = [[float('-inf')] * (n + 1) for _ in range(n)]
        right_best = [[float('-inf')] * (n + 1) for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r - 1] + prefix[r]
                )

                right_best[l][r] = max(
                    dp[l + 1][r] - prefix[l + 1],
                    right_best[l + 1][r]
                )

                total = prefix[r + 1] - prefix[l]

                p = bisect_right(prefix, (prefix[l] + prefix[r + 1]) // 2, l + 1, r + 1) - 1

                if p > l:
                    dp[l][r] = max(
                        dp[l][r],
                        left_best[l][p] - prefix[l]
                    )

                q = bisect_left(prefix, (prefix[l] + prefix[r + 1] + 1) // 2, l + 1, r + 1)

                if q <= r:
                    dp[l][r] = max(
                        dp[l][r],
                        right_best[q - 1][r] + prefix[r + 1]
                    )

        return dp[0][n - 1]