
from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)

        left, right = 0, diff[0]

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left

        operations = sum(max(0, d - level) for d in diff)

        ans = sum(min(d, level) ** 2 for d in diff)

        remaining = k - operations

        ans -= remaining * (2 * level - 1)

        return ans
