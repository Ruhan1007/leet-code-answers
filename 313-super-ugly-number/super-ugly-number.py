class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        indices = [0] * len(primes)

        for i in range(1, n):
            candidates = [primes[j] * dp[indices[j]] for j in range(len(primes))]
            dp[i] = min(candidates)

            for j in range(len(primes)):
                if candidates[j] == dp[i]:
                    indices[j] += 1

        return dp[-1]