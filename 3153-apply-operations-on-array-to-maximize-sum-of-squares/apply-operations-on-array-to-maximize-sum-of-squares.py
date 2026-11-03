class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        max_bits = 32
        cnt = [0] * max_bits
        for x in nums:
            for b in range(max_bits):
                if x >> b & 1:
                    cnt[b] += 1
        ans = 0
        for j in range(k):
            val = 0
            for b in range(max_bits):
                if j < cnt[b]:
                    val |= (1 << b)
            ans = (ans + val * val) % MOD
        return ans