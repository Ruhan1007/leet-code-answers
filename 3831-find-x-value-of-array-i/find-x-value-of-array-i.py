
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:

        ans = [0] * k

        # dp[r] = number of subarrays ending at the
        # previous index whose product % k == r
        dp = [0] * k

        for num in nums:
            num %= k

            new_dp = [0] * k

            # Start a new subarray with the current element
            new_dp[num] += 1

            # Extend all previous subarrays
            for r in range(k):
                new_rem = (r * num) % k
                new_dp[new_rem] += dp[r]

            # Add current subarray counts to the answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans
