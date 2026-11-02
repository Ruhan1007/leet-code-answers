class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, start, end, val):
            length = end - start + 1
            s = tree_sum[node]

            tree_sq[node] = (
                tree_sq[node] + 2 * val * s + length * val * val
            ) % MOD

            tree_sum[node] = (s + length * val) % MOD
            lazy[node] += val

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            mid = (start + end) // 2

            apply(node * 2, start, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, end, lazy[node])

            lazy[node] = 0

        def update(node, start, end, l, r):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                apply(node, start, end, 1)
                return

            push(node, start, end)

            mid = (start + end) // 2

            update(node * 2, start, mid, l, r)
            update(node * 2 + 1, mid + 1, end, l, r)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last_seen = {}
        ans = 0

        for i, num in enumerate(nums):
            prev = last_seen.get(num, -1)

            update(1, 0, n - 1, prev + 1, i)

            last_seen[num] = i

            ans = (ans + tree_sq[1]) % MOD

        return ans