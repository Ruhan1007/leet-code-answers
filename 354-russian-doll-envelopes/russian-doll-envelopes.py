class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        from bisect import bisect_left

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = []

        for w, h in envelopes:
            i = bisect_left(dp, h)

            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h

        return len(dp)
