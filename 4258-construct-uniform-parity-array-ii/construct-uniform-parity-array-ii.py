class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_odd = any(x % 2 == 1 for x in nums1)
        has_even = any(x % 2 == 0 for x in nums1)

        return not (has_odd and has_even) or min(nums1) % 2 == 1
