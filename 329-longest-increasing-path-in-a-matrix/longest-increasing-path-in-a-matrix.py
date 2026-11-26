class Solution:
    def longestIncreasingPath(self, matrix):
        from functools import lru_cache

        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i, j):
            ans = 1

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + di, j + dj

                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    ans = max(ans, 1 + dfs(x, y))

            return ans

        return max(dfs(i, j) for i in range(m) for j in range(n))