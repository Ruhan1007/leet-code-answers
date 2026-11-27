
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * n
        prev = [-1] * n

        max_len = 1
        last_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                last_index = i

        ans = []

        while last_index != -1:
            ans.append(nums[last_index])
            last_index = prev[last_index]

        return ans[::-1]
