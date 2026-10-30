class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0

        ans = -1

        for x in nums:
            if x != nums[x]:
                ans &= x

        return ans