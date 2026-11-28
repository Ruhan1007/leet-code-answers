class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        bonus = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                bonus[i] += freq[j]

            bonus[i] -= 1

        min_price = min(price for factor, price in items)

        arr = []

        for factor, price in items:
            if price <= 2 * min_price and bonus[factor] > 0:
                arr.append((price, bonus[factor]))

        arr.sort()

        ans = 0
        remaining = budget

        for price, count in arr:
            take = min(count, remaining // price)

            ans += 2 * take
            remaining -= take * price

        ans += remaining // min_price

        return ans