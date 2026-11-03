class Solution:
    def maxAlternatingSum(self, nums) -> int:
        abs_nums = sorted((abs(x) for x in nums), reverse=True)
        n = len(nums)
        p = (n + 1) // 2
        pos_sum = sum(x * x for x in abs_nums[:p])
        neg_sum = sum(x * x for x in abs_nums[p:])
        return pos_sum - neg_sum