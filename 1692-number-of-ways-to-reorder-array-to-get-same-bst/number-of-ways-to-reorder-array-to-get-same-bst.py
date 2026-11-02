class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations using Pascal's Triangle
        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = 1
            comb[i][i] = 1

            for j in range(1, i):
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            left_count = len(left)
            right_count = len(right)

            ways_left = solve(left)
            ways_right = solve(right)

            # Arrange left and right subtree elements
            ways = comb[left_count + right_count][left_count]

            return (ways * ways_left * ways_right) % MOD

        # Subtract 1 because the original ordering is also counted
        return (solve(nums) - 1) % MOD