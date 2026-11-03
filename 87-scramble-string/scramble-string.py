class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}

        def dfs(a, b):
            if a == b:
                return True
            if len(a) == 1:
                return False
            if sorted(a) != sorted(b):
                return False
            key = (a, b)
            if key in memo:
                return memo[key]

            n = len(a)
            for i in range(1, n):
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[key] = True
                    return True
                if dfs(a[:i], b[n - i:]) and dfs(a[i:], b[:n - i]):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(s1, s2)