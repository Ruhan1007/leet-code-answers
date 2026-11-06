class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        INF = n + 1
        min_end = [INF] * n
        
        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    if right < min_end[left]:
                        min_end[left] = right
                left -= 1
                right += 1
        
        dp = [0] * (n + 1)
        for i in range(n):
            if dp[i + 1] < dp[i]:
                dp[i + 1] = dp[i]
            if min_end[i] != INF:
                e = min_end[i]
                if dp[e + 1] < dp[i] + 1:
                    dp[e + 1] = dp[i] + 1
        
        return dp[n]