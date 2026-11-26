class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        mid = (len(nums) - 1) // 2
        left = nums[:mid + 1][::-1]
        right = nums[mid + 1:][::-1]

        nums[::2] = left
        nums[1::2] = right