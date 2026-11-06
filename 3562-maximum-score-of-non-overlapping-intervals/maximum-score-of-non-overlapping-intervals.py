
from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # Store original indices
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort intervals by starting position
        arr.sort()

        n = len(arr)
        starts = [x[0] for x in arr]

        # Find the next non-overlapping interval
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        @lru_cache(None)
        def dp(i, remaining):
            if i >= n or remaining == 0:
                return (0, ())

            # Option 1: Skip current interval
            skip_score, skip_indices = dp(i + 1, remaining)

            # Option 2: Take current interval
            take_score, take_indices = dp(next_idx[i], remaining - 1)

            take_score += arr[i][2]
            take_indices = tuple(sorted(take_indices + (arr[i][3],)))

            # Choose maximum score
            if take_score > skip_score:
                return (take_score, take_indices)

            if take_score < skip_score:
                return (skip_score, skip_indices)

            # Lexicographically smallest indices in case of tie
            return (take_score, min(take_indices, skip_indices))

        return list(dp(0, 4)[1])
