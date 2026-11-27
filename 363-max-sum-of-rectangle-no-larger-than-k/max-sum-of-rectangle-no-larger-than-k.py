
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        from bisect import bisect_left, insort

        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')

        for left in range(n):
            sums = [0] * m

            for right in range(left, n):
                for i in range(m):
                    sums[i] += matrix[i][right]

                prefix = 0
                prefixes = [0]

                for num in sums:
                    prefix += num

                    idx = bisect_left(prefixes, prefix - k)

                    if idx < len(prefixes):
                        ans = max(ans, prefix - prefixes[idx])

                    insort(prefixes, prefix)

                    if ans == k:
                        return k

        return ans
