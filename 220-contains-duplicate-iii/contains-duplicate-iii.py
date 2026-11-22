
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):
            bucket = num // width

            if bucket in buckets:
                return True

            if bucket - 1 in buckets and num - buckets[bucket - 1] <= valueDiff:
                return True

            if bucket + 1 in buckets and buckets[bucket + 1] - num <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // width
                del buckets[old_bucket]

        return False
