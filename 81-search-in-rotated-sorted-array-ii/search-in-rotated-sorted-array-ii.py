class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return True

            # Can't determine which side is sorted; shrink both ends
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:
                # Left half is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False