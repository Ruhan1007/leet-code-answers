
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * (n + 1) for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for i in range(d):
                        left = l + i
                        right = l + i + ((length - 1 - i) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[l][r + 1] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end]
                    )

        return dp[k][n]
