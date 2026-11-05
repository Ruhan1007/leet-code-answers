
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        pref = [[0] * k for _ in range(2 * size)]

        # Build leaf nodes
        for i in range(n):
            r = nums[i] % k
            prod[size + i] = r
            pref[size + i][r] = 1

        # Merge two nodes
        def merge(node):
            left = node * 2
            right = left + 1

            lp = prod[left]

            prod[node] = (lp * prod[right]) % k

            # Start with left child's prefix frequencies
            for r in range(k):
                pref[node][r] = pref[left][r]

            # Add right child's prefixes
            for r in range(k):
                new_rem = (lp * r) % k
                pref[node][new_rem] += pref[right][r]

        # Build segment tree
        for i in range(size - 1, 0, -1):
            merge(i)

        ans = []

        for index, value, start, x in queries:

            # Update element
            p = size + index
            r = value % k

            prod[p] = r
            pref[p] = [0] * k
            pref[p][r] = 1

            p //= 2

            while p:
                merge(p)
                p //= 2

            # Query range [start, n-1]
            l = start + size
            r = n + size

            left_nodes = []
            right_nodes = []

            while l < r:
                if l & 1:
                    left_nodes.append(l)
                    l += 1

                if r & 1:
                    r -= 1
                    right_nodes.append(r)

                l //= 2
                r //= 2

            nodes = left_nodes + right_nodes[::-1]

            # Count valid non-empty prefixes
            current = 1
            count = 0

            for node in nodes:

                for rem in range(k):
                    if (current * rem) % k == x:
                        count += pref[node][rem]

                current = (current * prod[node]) % k

            ans.append(count)

        return ans
