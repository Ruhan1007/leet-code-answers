
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        weights = []

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    count += 1
            weights.append(count + 1)

        groups = {}
        for i, (factor, price) in enumerate(items):
            groups.setdefault(price, []).append(weights[i])

        dp = [0] * (budget + 1)
        ans = 0

        for price in sorted(groups, reverse=True):
            current = [-1] * (budget + 1)

            for weight in groups[price]:
                for cost in range(budget, price - 1, -1):
                    if dp[cost - price] > -1:
                        current[cost] = max(
                            current[cost],
                            dp[cost - price] + weight
                        )

                    if current[cost - price] > -1:
                        current[cost] = max(
                            current[cost],
                            current[cost - price] + weight
                        )

            for cost in range(budget + 1):
                if current[cost] >= 0:
                    ans = max(
                        ans,
                        current[cost] + (budget - cost) // price
                    )

            for weight in groups[price]:
                for cost in range(budget, price - 1, -1):
                    dp[cost] = max(
                        dp[cost],
                        dp[cost - price] + weight
                    )

        return ans
