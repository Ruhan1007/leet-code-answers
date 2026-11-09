class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
        
        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(1, i + 1):
                    if is_pal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        
        return dp[n - 1]